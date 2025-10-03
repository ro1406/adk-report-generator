"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
agent.py (c) 2025
Desc: description
Created:  2025-09-29T16:50:49.682Z
Modified: 2025-10-03T21:01:37.500Z
"""

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import load_artifacts

from .prompt import INTERFACE_AGENT_PROMPT
from .sub_agents.data_retriever_agent import data_retriever_agent
from .sub_agents.summarizer_agent import summarizer_agent

MODEL = "gemini-2.5-flash"

workflow_executor_agent = SequentialAgent(
    name="workflow_executor_agent",
    sub_agents=[data_retriever_agent, summarizer_agent],
    description="A sequential agent that executes the data retrieval and summarization agents in sequence.",
)


root_agent = LlmAgent(
    name="interface_agent",
    model=MODEL,
    description="A professional financial analysis interface agent that coordinates comprehensive stock market analysis by collecting user requirements (stock symbol and date range) and executing a sequential workflow of data retrieval and analysis agents to provide actionable trading insights.",
    instruction=INTERFACE_AGENT_PROMPT,
    output_key="interface_agent_output",
    tools=[
        AgentTool(agent=workflow_executor_agent),
        load_artifacts,
    ],
)
