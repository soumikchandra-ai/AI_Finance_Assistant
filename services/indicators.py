import yfinance as yf
import pandas as pd
import numpy as np
import ta

#To load the financial data
def load_data(symbol:str,period:str="6mo"):
    df=yf.download(symbol,period=period)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)
    df=df.reset_index()
    return df

#To calculate the Simple Moving average
def add_sma(df,window=20):
    df[f"sma_{window}"]=df["Close"].rolling(window=window).mean()
    return df

#To calculate the Exponential Moving Average
def add_ema(df,window=20):
    df[f"ema_{window}"]=df["Close"].ewm(span=window,adjust=False).mean()
    return df

#To find the RSI
def add_rsi(df, window=14):
    close=df["Close"].squeeze()
    df["RSI"] = ta.momentum.RSIIndicator(
        close=close,
        window=window
    ).rsi()
    return df

#To show momentum indicator
def add_macd(df):
    macd=ta.trend.MACD(df["Close"])
    
    df["MACD"]=macd.macd()                  #MACD
    df["MACD_Signal"]=macd.macd_signal()    #Signal Line
    df["MACD_Diff"]=macd.macd_diff()        #Histogram
    
    return df

def generate_signal(df):
    latest=df.iloc[-1]
    
    rsi=latest["RSI"]
    macd=latest["MACD"]
    signal=latest["MACD_Signal"]
    
    recommendation="HOLD"

    if rsi<30 and macd>signal:
        recommendation="BUY(Strong)"
        
    elif rsi<30 and macd<signal:
        recommendation="SELL(Strong)"
    
    elif macd>signal:
        recommendation="BUY(Weak)"
        
    elif macd<signal:
        recommendation="SELL(Weak)"
        
    return {
        "rsi":float(rsi),
        "macd":float(macd),
        "macd_signal":float(signal),
        "recommendation":recommendation
    }
    
#Final indicator engine
def analyze_stock(symbol:str):
    
    #Data loading
    df=load_data(symbol)
    
    #Add sma
    df=add_sma(df)
    
    #Add ema
    df=add_ema(df)
    
    #Add rsi
    df=add_rsi(df)
    
    #Add macd
    df=add_macd(df)
    
    #Genearting the signal to take decision
    
    signal=generate_signal(df)
    
    return{
        "symbol":symbol,
        "latest_close":float(df["Close"].iloc[-1]),
        "signals":signal,
        "data":df.tail(10).to_dict(orient="records")
    }
    
