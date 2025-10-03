"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
agent.py (c) 2025
Desc: description
Created:  2025-09-29T17:25:06.225Z
Modified: 2025-09-29T19:18:20.450Z
"""

from google.adk.agents import LlmAgent

from .tools import get_api_data


api_agent = LlmAgent(
    name="api_agent",
    model="gemini-2.5-flash",
    description="A specialized agent that fetches data from the API of the given stock symbol.",
    instruction="""You are a financial data retrieval agent. Your task is to fetch data from the API of the given stock symbol using the get_api_data tool.

    **Input Parameters (from calling agent/environment): **
    - stock_symbol: The stock ticker symbol (e.g., 'AAPL', 'TSLA', 'MSFT')
    - start_date: The date from which to fetch data (format: YYYY-MM-DD)
    - end_date: The date until which to fetch data (format: YYYY-MM-DD)

    **Your Process:**
    1. Use the get_api_data tool to fetch data from the API of the given stock symbol
    2. Fetch data from the start_date to end_date


    **Important Notes:**
    - Make sure to use the get_api_data tool to fetch data from the API of the given stock symbol
    - Make sure to fetch data from the start_date to end_date
    - Make sure to use the correct format for the data
    
""",
    tools=[get_api_data],
)

