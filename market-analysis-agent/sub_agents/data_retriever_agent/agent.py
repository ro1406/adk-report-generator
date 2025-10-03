"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
agent.py (c) 2025
Desc: description
Created:  2025-09-29T16:54:14.650Z
Modified: 2025-09-29T19:29:32.639Z
"""

from google.adk.agents import ParallelAgent
from .data_sub_agents.news_agent.agent import news_agent
from .data_sub_agents.api_agent.agent import api_agent


data_retriever_agent = parallel_research_agent = ParallelAgent(
    name="ParallelDataRetrieverAgent",
    sub_agents=[news_agent, api_agent],
    description="Runs multiple data fetching agents in parallel to gather information about the given stock in the stock market.",
)
