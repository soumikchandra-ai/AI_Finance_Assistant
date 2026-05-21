import yfinance as yf
import pandas as pd

def get_stock_info(symbol:str):
    stock=yf.Ticker(symbol)
    info=stock.info
    
    return{
        "symbol":symbol,
        "name":info.get("shortName"),
        "sector":info.get("sector"),
        "marketPrice":info.get("regularMarketPrice"),
        "currency":info.get("currency"),
        "marketcap":info.get("marketcap"),
    }
    
def get_historical_data(symbol:str,period:str):
    stock=yf.Ticker(symbol)
    
    df=stock.history(period=period)
    
    df=df.reset_index()
    return df[["Date","Open","High","Low","Close","Volume"]].to_dict(orient="records")
