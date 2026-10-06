import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from src.data.fred import FredDataClient
from src.ai.analyzer import EconomicAnalyzer

st.set_page_config(page_title="Macro Overview", page_icon="🌍", layout="wide")

st.title("🌍 Macroeconomic Overview")
st.markdown("Track the 'Big Three' economic indicators driving monetary policy.")

@st.cache_data
def load_core_metrics():
    client = FredDataClient()
    unrate = client.get_series('UNRATE')
    fedfunds = client.get_series('FEDFUNDS')
    cpi = client.get_series('CPIAUCSL')
    
    # Advanced Data Engineering: Calculate Year-over-Year Inflation from raw CPI index
    if cpi is not None and not cpi.empty:
        cpi['value'] = cpi['value'].pct_change(12) * 100
        cpi = cpi.dropna() 
        
    return unrate, fedfunds, cpi

with st.spinner("Authenticating with Federal Reserve and fetching live data..."):
    unrate, fedfunds, cpi = load_core_metrics()

if unrate is not None and fedfunds is not None and cpi is not None:
    # Top Row: KPI Metrics
    st.subheader("Current Core Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("Unemployment Rate", f"{unrate.iloc[-1]['value']:.1f}%")
    col2.metric("YoY Inflation (CPI)", f"{cpi.iloc[-1]['value']:.1f}%")
    col3.metric("Fed Funds Rate", f"{fedfunds.iloc[-1]['value']:.2f}%")
    
    st.divider()
    
    # Middle Row: Interactive Plotly Chart
    st.subheader("Historical Trends (10-Year View)")
    fig = go.Figure()
    
    # Filter data for the last 10 years for a clean chart
    ten_years_ago = pd.Timestamp.now() - pd.DateOffset(years=10)
    u_plot = unrate[unrate['date'] >= ten_years_ago]
    c_plot = cpi[cpi['date'] >= ten_years_ago]
    f_plot = fedfunds[fedfunds['date'] >= ten_years_ago]

    # Add sophisticated interactive lines
    fig.add_trace(go.Scatter(x=u_plot['date'], y=u_plot['value'], name='Unemployment', line=dict(color='#3498DB', width=2.5)))
    fig.add_trace(go.Scatter(x=c_plot['date'], y=c_plot['value'], name='Inflation (YoY)', line=dict(color='#E74C3C', width=2.5)))
    fig.add_trace(go.Scatter(x=f_plot['date'], y=f_plot['value'], name='Interest Rate', line=dict(color='#2ECC71', width=2.5)))
    
    # Professional chart styling
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(showgrid=True, gridcolor='lightgrey', title="Percentage (%)")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Bottom Row: AI Analysis
    st.subheader("🤖 AI Chief Economist Analysis")
    ai = EconomicAnalyzer()
    summary = ai.generate_executive_summary({
        "unemployment": round(unrate.iloc[-1]['value'], 1),
        "inflation": round(cpi.iloc[-1]['value'], 1),
        "interest_rate": round(fedfunds.iloc[-1]['value'], 2)
    })
    st.info(summary)
else:
    st.error("⚠️ Failed to load data. Check API keys and connection.")
    