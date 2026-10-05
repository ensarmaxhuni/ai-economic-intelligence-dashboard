from src.utils.logger import get_logger

logger = get_logger(__name__)

class EconomicAnalyzer:
    """
    Simulated AI Client for generating economic summaries.
    In a production environment, this would connect to the OpenAI API.
    """
    
    def __init__(self):
        logger.info("Initializing Simulated Economic AI Analyzer.")

    def generate_executive_summary(self, data_context: dict) -> str:
        """Generates a professional mock executive summary based on the data."""
        logger.info("Generating simulated AI executive summary...")
        
        # Safely grab data if provided, otherwise use placeholders
        unemployment = data_context.get("unemployment", "N/A")
        
        summary = (
            f"📊 **Executive Economic Summary**\n\n"
            f"Based on the latest data inputs, the macroeconomic environment is demonstrating structural resilience. "
            f"The current unemployment rate sits at **{unemployment}%**, indicating a stabilizing labor market following recent cyclical shifts.\n\n"
            f"**Key Takeaways:**\n"
            f"- **Labor Market:** Stable workforce participation with controlled unemployment.\n"
            f"- **Monetary Policy Impact:** Current indicators suggest previous interest rate adjustments are effectively balancing growth and inflation.\n"
            f"- **Outlook:** Cautiously optimistic. Continued monitoring of consumer spending and inflation core metrics is advised over the next quarter."
        )
        
        return summary
        