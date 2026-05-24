# Finance AI — Intelligent Financial Analysis Platform

> A production-grade, AI-powered financial research terminal combining real-time market data, technical analysis, portfolio intelligence, and generative AI to surface actionable investment insights.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?logo=google)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Author](#author)

---

## Overview

Finance AI bridges the gap between fragmented financial tooling and cohesive, AI-driven decision support. Rather than switching between charting platforms, indicator calculators, and news aggregators, analysts get a unified terminal that ingests real-time market data, computes technical signals, and synthesises everything through a large language model into clear, actionable recommendations.

Think of it as a lightweight Bloomberg terminal — without the six-figure subscription.

---

## Features

### Stock Analysis
- Real-time price fetching and historical OHLCV processing via `yfinance`
- Full technical indicator suite: RSI, MACD, SMA, EMA
- Automated Buy / Sell / Hold signal generation

### Portfolio Analytics
- Multi-asset portfolio ingestion and performance evaluation
- Expected return estimation and annualised volatility calculation
- Correlation matrix for diversification and concentration risk analysis

### AI Financial Assistant
- Conversational Q&A powered by Google Gemini
- Plain-language explanations of complex instruments and market events
- Context-aware investment insights suitable for all experience levels

### Automated Report Generation
- Professional PDF reports built with ReportLab
- AI-generated narrative summaries embedded alongside quantitative data
- One-click download for sharing and archiving

### Interactive Visualisation
- Responsive Chart.js dashboards for price trends, RSI, and MACD
- Portfolio performance attribution charts

---

## Architecture

```
┌──────────────────────────────────────┐
│           Frontend (Browser)         │
│   HTML5 · CSS3 · JavaScript · Chart.js │
└───────────────────┬──────────────────┘
                    │ HTTP / REST
┌───────────────────▼──────────────────┐
│           FastAPI Application        │
│              (backend/main.py)       │
└──┬────────────┬──────────┬───────────┘
   │            │          │
   ▼            ▼          ▼
Market Data  Technical   AI Layer
(yfinance)  Indicators  (Gemini API)
            (ta lib)
   │            │          │
   └────────────┴──────────┘
                │
        ┌───────▼────────┐
        │  Report Engine │
        │  (ReportLab)   │
        └───────┬────────┘
                │
        JSON / PDF Response
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, CSS3,  Chart.js |
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **Market Data** | yfinance, pandas, numpy |
| **Indicators** | ta (Technical Analysis Library) |
| **AI** | Google Gemini API (`gemini-2.5-flash`) |
| **Reporting** | ReportLab |

---

## Project Structure

```
finance-ai/
├── backend/
│   └── main.py                  # FastAPI app, route definitions, middleware
│
├── services/
│   ├── stock_service.py         # yfinance data fetching and preprocessing
│   ├── indicators.py            # RSI, MACD, SMA, EMA computation
│   ├── portfolio_service.py     # Returns, volatility, correlation matrix
│   ├── ai_service.py            # Gemini API client and prompt management
│   └── report_service.py        # PDF generation with ReportLab
│
├── frontend/
│   ├── index.html               # App shell and layout
│   ├── style.css                # Styles and responsive design
│   └── script.js                # API calls, chart rendering, UI logic
│
├── .env                         # Environment variables (never commit)
├── requirements.txt
└── README.md
```

---

## API Reference

### `GET /analysis/{symbol}`

Returns technical indicators, an AI-generated narrative, and a trade signal for the given ticker.

**Path parameter:** `symbol` — e.g. `AAPL`, `MSFT`, `TSLA`

**Response**
```json
{
  "symbol": "AAPL",
  "price": 213.49,
  "indicators": {
    "rsi": 58.3,
    "macd": 1.24,
    "sma_20": 209.10,
    "ema_20": 211.85
  },
  "signal": "BUY",
  "ai_summary": "Apple is trading above its 50-day SMA with a neutral RSI..."
}
```

---

### `GET /portfolio`

Analyses a basket of tickers and returns portfolio-level risk and return metrics.

**Query parameters:** `symbols` (repeatable) — e.g. `?symbols=AAPL&symbols=MSFT&symbols=TSLA`

**Response**
```json
{
  "expected_annual_return": 0.182,
  "annual_volatility": 0.241,
  "correlation_matrix": { ... },
  "ai_summary": "The portfolio exhibits moderate concentration risk..."
}
```

---

### `POST /chat`

Sends a natural-language message to the AI financial assistant.

**Request body**
```json
{
  "message": "Should I invest in Tesla given current macro conditions?"
}
```

**Response**
```json
{
  "reply": "Tesla's high beta makes it sensitive to interest rate movements..."
}
```

---

### `GET /generate-report/{symbol}`

Generates and returns a downloadable PDF report for the requested ticker.

**Response:** `application/pdf`

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- A [Google AI Studio](https://aistudio.google.com) API key

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/finance-ai.git
cd finance-ai

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables (see Configuration below)
cp .env.example .env

# 5. Start the development server
uvicorn backend.main:app --reload

# 6. Open the application
# Navigate to http://127.0.0.1:8000 in your browser
```

---

## Configuration

Create a `.env` file in the project root with the following variables:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> **Never commit `.env` to version control.** The `.gitignore` in this repository excludes it by default.

---

## Author

**Soumik Chandra**

Built to demonstrate full-stack AI engineering, real-world financial system design, and end-to-end LLM integration in a production-grade architecture.

---

*Contributions, issues, and feature requests are welcome.*
