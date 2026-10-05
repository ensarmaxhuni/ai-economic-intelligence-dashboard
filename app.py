import streamlit as st
from src.data.fred import FredDataClient
from src.ai.analyzer import EconomicAnalyzer

# Configure the page layout
st.set_page_config(page_title="AI Economic Intelligence", page_icon="📈", layout="wide")

st.title("📈 AI Economic Intelligence Dashboard")
st.markdown("Real-time macroeconomic data and AI-driven executive analysis.")
st.divider()

# Cache the data so it doesn't re-download every time you click a button
@st.cache_data
def load_data():
    client = FredDataClient()
    return client.get_series('UNRATE')

# Fetch the data
df = load_data()

if df is not None and not df.empty:
    # Get the most recent unemployment rate
    latest_unemployment = df.iloc[-1]['value']
    
    # Create two columns: 70% width for the chart, 30% width for the AI
    col1, col2 = st.columns([0.7, 0.3])
    
    with col1:
        st.subheader("US Unemployment Rate")
        # Streamlit makes beautiful charts with one line of code
        st.line_chart(df.set_index('date')['value'])
        
    with col2:
        st.subheader("AI Analysis")
        # Initialize our mock AI and generate the summary
        ai = EconomicAnalyzer()
        summary = ai.generate_executive_summary({"unemployment": latest_unemployment})
        
        # Display the AI summary in an info box
        st.info(summary)
else:
    st.error("⚠️ Failed to load data from the FRED API. Please check your API key and connection.")
    