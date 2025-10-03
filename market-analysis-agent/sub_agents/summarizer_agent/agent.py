"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
agent.py (c) 2025
Desc: description
Created:  2025-09-29T19:00:22.968Z
Modified: 2025-10-03T21:01:56.642Z
"""

from .prompt import SUMMARIZER_AGENT_PROMPT
from google.adk.agents import LlmAgent
from google.adk.tools import load_artifacts


summarizer_agent = LlmAgent(
    name="summarizer_agent",
    model="gemini-2.5-pro",
    description="A comprehensive analysis agent that combines news sentiment with stock price trends to provide actionable trading insights and recommendations.",
    instruction=SUMMARIZER_AGENT_PROMPT,
    tools=[load_artifacts],
    output_key="summarizer_agent_output",
)
