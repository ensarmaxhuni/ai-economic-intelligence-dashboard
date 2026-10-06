# 🏛️ AI Economic Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FRED API](https://img.shields.io/badge/Data-FRED_API-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

An enterprise-grade macroeconomic data dashboard that aggregates real-time data from the Federal Reserve (FRED) and leverages Artificial Intelligence to generate institutional-grade market analysis.

## 🚀 Key Features

* **Real-Time Data Ingestion:** Automated fetching of the "Big Three" economic indicators (Unemployment, CPI/Inflation, and Federal Funds Rate) directly from the US Government's FRED API.
* **Advanced Data Engineering:** On-the-fly calculation of Year-over-Year (YoY) metrics and data cleaning using `pandas`.
* **Interactive Visualizations:** Highly responsive, hoverable, multi-line financial charts built with `plotly.graph_objects`.
* **AI Chief Economist:** Simulated AI integration that synthesizes raw metrics into professional, forward-looking executive summaries.
* **Enterprise Architecture:** Built with a modular, scalable backend and an explicit multi-page Streamlit frontend.

## 🛠️ Technology Stack

* **Backend & Math:** Python, Pandas, Numpy
* **Frontend UI:** Streamlit
* **Visualizations:** Plotly
* **APIs:** Federal Reserve Economic Data (FRED), Simulated OpenAI Endpoint
* **Version Control:** Git, GitHub

## 📂 Project Structure

```text
ai-economic-intelligence-dashboard/
├── .env                  # Secure API keys (git-ignored)
├── app.py                # Main Streamlit application and routing
├── requirements.txt      # Project dependencies
├── src/                  # Backend modules
│   ├── ai/               # AI analysis engine
│   │   └── analyzer.py 
│   ├── data/             # Data ingestion layer
│   │   └── fred.py     
│   └── utils/            # Logging and configuration
│       ├── config.py   
│       └── logger.py   
└── pages/                # Streamlit auto-routing directory (legacy backup)
