from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    return {"message":"Finance AI Backend Running"}

@app.get('/health')
def health():
    return {"status":"OK"}