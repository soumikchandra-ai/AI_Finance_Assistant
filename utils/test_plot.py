import yfinance as yf
import matplotlib.pyplot as plt
from services.stock_service import get_historical_data

def plot_historical_data(symbol:str,period:str):
    data=get_historical_data(symbol,period)
    
    closes=[row["Close"] for row in data]
    
    plt.plot(closes)
    plt.title(f"Closing prices for {symbol}")
    plt.show()
    
plot_historical_data("AAPL","1mo")