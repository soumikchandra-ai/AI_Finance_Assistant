from fastapi import FastAPI
from services.stock_service import get_stock_info,get_historical_data

app=FastAPI()

@app.get('/')
def home():
    return {"message":"Finance AI Backend Running"}

@app.get('/stock/{symbol}')
def stock_info(symbol:str):
    return get_stock_info(symbol)


@app.get('/history/{symbol}')
def stock_history_info(symbol:str,period:str):
    return get_historical_data(symbol,period)
