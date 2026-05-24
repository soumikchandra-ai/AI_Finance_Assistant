from fastapi import FastAPI,Query
from services.stock_service import get_stock_info,get_historical_data
from services.indicators import analyze_stock
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from services.ai_service import generate_ai_analysis
from services.portfolio_service import analyze_portfolio
from pydantic import BaseModel
from services.ai_service import finance_chat
from services.report_service import generate_pdf_report
import os
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

class ChatRequest(BaseModel):
    
    message:str

app.mount("/static",StaticFiles(directory="frontend"),name="static")


@app.get('/')
def serve_home():
    return FileResponse("frontend/index.html")

@app.get('/stock/{symbol}')
def stock_info(symbol:str):
    return get_stock_info(symbol)


@app.get('/history/{symbol}')
def stock_history_info(symbol:str,period:str):
    return get_historical_data(symbol,period)

@app.get("/analysis/{symbol}")
def analysis(symbol:str):
    try:
        stock_data=analyze_stock(symbol)
    
        ai_analysis=generate_ai_analysis(stock_data)
    
        return {
            "stock_data":stock_data,
            "ai_analysis":ai_analysis
        }
    except Exception as e:
        return {
            "error":str(e)
        }
    
    
@app.get('/portfolio')
def portfolio_analysis(symbols:list[str]=Query(...)):
    return analyze_portfolio(symbols)

@app.post('/chat')
def chat(request:ChatRequest):
    response=finance_chat(request.message)
    return{
        "response":response
    }
    
@app.get('/generate-report/{symbol}')
def create_report(symbol:str):
    stock_data=analyze_stock(symbol)
    ai_analysis=generate_ai_analysis(stock_data)
    
    filename=generate_pdf_report(
        symbol,
        stock_data,
        ai_analysis
    )
    return FileResponse(
        path=filename,
        media_type="application/pdf",
        filename=filename
    )
    