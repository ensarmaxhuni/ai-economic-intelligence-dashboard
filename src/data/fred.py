import os
import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

class FredDataClient:
    def __init__(self):
        # 1. Check Streamlit Cloud Secrets first
        if hasattr(st, "secrets") and "FRED_API_KEY" in st.secrets:
            self.api_key = st.secrets["FRED_API_KEY"]
        else:
            # 2. Fallback to local environment variable
            self.api_key = os.getenv("FRED_API_KEY")
            
        self.base_url = "https://api.stlouisfed.org/fred/series/observations"

    def get_series(self, series_id: str) -> pd.DataFrame:
        if not self.api_key:
            st.error("FRED_API_KEY not found in Streamlit Secrets or .env file.")
            return None

        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json"
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            observations = data.get("observations", [])
            if not observations:
                return None

            df = pd.DataFrame(observations)[["date", "value"]]
            df["date"] = pd.to_datetime(df["date"])
            df["value"] = pd.to_numeric(df["value"], errors="coerce")
            df = df.dropna()
            return df

        except Exception as e:
            st.error(f"Error fetching {series_id}: {e}")
            return None
