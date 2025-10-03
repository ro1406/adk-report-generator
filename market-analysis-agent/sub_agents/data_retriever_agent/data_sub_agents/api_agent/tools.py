"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
tools.py (c) 2025
Desc: description
Created:  2025-09-29T17:25:34.452Z
Modified: 2025-10-03T21:11:11.072Z
"""

# import contextlib
from datetime import datetime

# import io
import re

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import json
from google.adk.tools import ToolContext
from google.genai import types


def is_valid_ticker(ticker: str) -> bool:
    try:
        info = yf.Ticker(ticker).get_info()
        return bool(info and "symbol" in info)
    except Exception:
        return False


async def get_api_data(
    stock_symbol: str, start_date: str, end_date: str, tool_context: ToolContext
) -> dict[str, dict[str, str]]:
    """
    Fetches data from the API of the given stock symbol. Saves the fetched data to artifacts as a json object (dict).

    Args:
        stock_symbol (str): The stock ticker symbol (e.g., 'AAPL', 'TSLA', 'MSFT')
        start_date (str): The date from which to fetch data (format: YYYY-MM-DD)
        end_date (str): The date until which to fetch data (format: YYYY-MM-DD)

    Returns:
        dict: A dictionary with the status and the error_message if any
    """

    # Verify that start date and end date should be in YYYY-MM-DD
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", start_date) or not re.match(r"^\d{4}-\d{2}-\d{2}$", end_date):
        return {
            "status": "error",
            "error_message": "Start date and end date must be in YYYY-MM-DD format",
        }

    # Verify that stock symbol is a valid stock symbol
    if not is_valid_ticker(stock_symbol):
        return {"status": "error", "error_message": f"Invalid stock symbol: '{stock_symbol}'"}

    try:
        data = yf.download(stock_symbol, start=start_date, end=end_date)
    except Exception as e:
        return {"status": "error", "error_message": f"Error fetching data: {e}"}

    # Remove the multi-index columns - Mainly removes the ticker name
    data.columns = data.columns.get_level_values(0)

    return_data = json.loads(data.reset_index().to_json(orient="records", date_format="iso"))

    # Save the data fetched to artifacts
    await tool_context.save_artifact("yfinance_data_json", return_data)

    # Try to save into tool context instead
    # tool_context.state["finance_df"] = return_data

    return {"status": "success", "error_message": None}
