import yfinance as yf
import pandas as pd
from services.ai_service import generate_portfolio_analysis

def load_portfolio_data(symbols,period="6mo"):
    
    data={}
    
    for symbol in symbols:
        df=yf.download(symbol,period=period,group_by="tickers")
        if "Close" in df.columns:
            data[symbol] = df["Close"].squeeze()
        else:
            data[symbol] = df[symbol]["Close"].squeeze()
            
    return pd.DataFrame(data)
    
def calculate_return(df):
    returns=df.pct_change()
    returns=returns.dropna()
    return returns

#Assuming all stocks weighted equally

def portfolio_return(returns):
    daily_portfolio_returns=returns.mean(axis=1)
    return float(daily_portfolio_returns.mean())

def portfolio_risk(returns):
    daily_portfolio_returns=returns.mean(axis=1)
    return float(daily_portfolio_returns.std())

def portfolio_correlation(returns):
    correlation=returns.corr()
    return correlation.to_dict()

def analyze_portfolio(symbols):
    
    #Load the portfolio data
    df=load_portfolio_data(symbols)
    
    #Load the returns
    returns=calculate_return(df)
    
    #Load the portfolio returns
    expected_return=portfolio_return(returns)
    
    #Load the portfolio risk
    risk=portfolio_risk(returns)
    
    #Load the correlation among the portfolio
    correlation=portfolio_correlation(returns)
    
    portfolio_data={
        "stocks":symbols,
        "expected_return":expected_return,
        "risk":risk,
        "correlation":correlation
    }
    
    ai_analysis=generate_portfolio_analysis(portfolio_data)
    
    return {
        "portfolio_metrics":portfolio_data,
        "ai_analysis":ai_analysis
    }
    