import streamlit as st
import requests

st.title("AI Finance Analyst Dashboard")

st.write("Welcome to your AI Finance Assistant")

stock=st.text_input("Enter your ticker (e.g. AAPL)")

if st.button("Get Backend Data"):
    res=requests.get("http://127.0.0.1:8000")
    st.write(res.json())