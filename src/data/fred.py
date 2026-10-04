import httpx
import pandas as pd
from typing import Optional
from src.utils.config import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

class FredDataClient:
    """Client for securely fetching data from the FRED API."""
    
    BASE_URL = "https://api.stlouisfed.org/fred"

    def __init__(self):
        self.api_key = settings.FRED_API_KEY
        if not self.api_key:
            logger.error("FRED API key is missing from the environment!")

    def get_series(self, series_id: str) -> Optional[pd.DataFrame]:
        """Fetches a time series from FRED and returns it as a pandas DataFrame."""
        endpoint = f"{self.BASE_URL}/series/observations"
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
        }

        try:
            logger.info(f"Fetching data for FRED series: {series_id}")
            # We use httpx for modern, fast API requests with a strict 10-second timeout
            with httpx.Client(timeout=10.0) as client:
                response = client.get(endpoint, params=params)
                response.raise_for_status()
                
                data = response.json()
                observations = data.get("observations", [])
                
                if not observations:
                    logger.warning(f"No data found for series: {series_id}")
                    return None
                    
                # Convert the raw JSON data into a clean Pandas DataFrame
                df = pd.DataFrame(observations)
                df['date'] = pd.to_datetime(df['date'])
                
                # Clean up FRED's missing data markers (they use a period '.' for missing)
                df = df[df['value'] != '.']
                df['value'] = df['value'].astype(float)
                
                # Keep only what we need and sort it chronologically
                df = df[['date', 'value']].sort_values('date').reset_index(drop=True)
                
                logger.info(f"Successfully loaded {len(df)} records for {series_id}")
                return df

        except httpx.HTTPError as e:
            logger.error(f"HTTP connection error while fetching {series_id}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected data processing error for {series_id}: {e}")
            return None 
