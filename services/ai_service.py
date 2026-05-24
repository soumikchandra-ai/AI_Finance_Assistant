import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

def generate_ai_analysis(stock_data):
    try:
        
        prompt = f"""
        You are an expert financial analyst.

        Analyze the following stock data and provide:

        1. Trend analysis
        2. Risk analysis
        3. Investment recommendation
        4. Explanation of RSI and MACD
        5. Short-term outlook

        Stock Data:
        {stock_data}

        Give beginner-friendly explanation.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    except Exception as e:
        print("Gemini error:", e)
        return "Sorry, AI service is temporarily unavailable."
        

def generate_portfolio_analysis(portfolio_data):

    prompt = f"""
    You are a professional portfolio analyst.

    Analyze this investment portfolio.

    Give:
    1. Portfolio diversification analysis
    2. Risk assessment
    3. Strengths and weaknesses
    4. Long-term outlook
    5. Suggestions for improvement

    Portfolio Data:
    {portfolio_data}

    Explain in beginner-friendly language.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

def finance_chat(user_message):
    prompt=f"""
    You are an AI financial assistant.

    Your job is to:
    - Explain finance concepts simply
    - Analyze stocks
    - Explain RSI, MACD, trends
    - Help beginner investors
    - Compare companies
    - Give educational insights

    DO NOT give guaranteed financial advice.

    User Question:
    {user_message}

    Give a clear beginner-friendly answer.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
