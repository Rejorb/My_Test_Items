import streamlit as st
import requests
import json
from fastapi import FastAPI
import uvicorn

st.title("Calculator App")
st.write("This app connects to Render")

app = FastAPI()

@app.get("/add")
def add(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return {"operation": "add", "a": a, "b": b, "result": result}

@app.get("/subtract")
def subtract(a, b):
    """Subtract b from a and return the result."""
    result = a - b
    return {"operation": "subtract", "a": a, "b": b, "result": result}

@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Calculator API is running. Use /add or /subtract endpoints."}


# Main program
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9321)

#api_url = "https://genaiengineering-cohort1-xe38.onrender.com"

