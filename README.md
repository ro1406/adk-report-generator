# ADK Workshop: "It Starts with a Stock Bot - Agentic AI Design Pattern"

This repository contains the code and examples presented at the workshop **"It Starts with a Stock Bot: An Agentic AI Design Pattern for Scalable AI Workflows"** at Google Developer Group DevFest 2025, held at Google HQ Dubai.

## Overview

This workshop demonstrates how to build scalable AI workflows using Google's Agent Development Kit (ADK) through practical examples. The repository showcases various AI agents that solve real-world problems, from financial analysis to creative tasks and research assistance.

## 🚀 Quick Start

To run any of the agents with a web interface, use:

```bash
adk web
```

This will start the ADK web interface at `http://127.0.0.1:8000/dev-ui/` where you can interact with all the available agents.

## 📁 Repository Structure

### Market Analysis Agent (Stock Bot) 🏦
**Location:** `adk-report-generator/market-analysis-agent/`

The main example from the workshop - a sophisticated financial analysis system that demonstrates the agentic AI design pattern for scalable AI workflows.

**Features:**
- **Stock Data Retrieval**: Fetches real-time stock data using Yahoo Finance API
- **News Analysis**: Analyzes market sentiment and news impact  
- **Technical Analysis**: Provides comprehensive technical indicators and trends
- **Report Generation**: Creates detailed investment reports with actionable insights

**Agent Architecture:**
- **Interface Agent**: Coordinates user interactions and workflow execution
- **Data Retriever Agent**: Handles stock data collection and news gathering
  - **API Agent**: Specialized sub-agent for Yahoo Finance data retrieval
  - **News Agent**: Specialized sub-agent for news analysis and sentiment
- **Summarizer Agent**: Processes and analyzes collected data into comprehensive reports

**File Structure:**
```
adk-report-generator/
├── market-analysis-agent/
│   ├── agent.py                    # Main interface agent
│   ├── prompt.py                   # Agent instructions and prompts
│   └── sub_agents/
│       ├── data_retriever_agent/
│       │   ├── agent.py            # Data collection coordinator
│       │   └── data_sub_agents/
│       │       ├── api_agent/      # Yahoo Finance API integration
│       │       └── news_agent/     # News analysis and sentiment
│       └── summarizer_agent/
│           ├── agent.py            # Report generation agent
│           └── prompt.py           # Analysis instructions
├── lol.ipynb                       # Jupyter notebook for testing
└── README.md
```

## 🛠️ Prerequisites

- **Python 3.8+**
- **Google Cloud Project** with Vertex AI enabled
- **ADK (Agent Development Kit)** installed
- **Google Cloud Credentials** properly configured

## 📋 Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
```

2. **Install ADK and dependencies:**
```bash
pip install google-adk
```

3. **Set up Google Cloud credentials:**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

4. **Configure environment variables:**
Each project contains an `env.example` file. Copy it to `.env` and configure:
```bash
cp env.example .env
# Edit .env with your Google Cloud configuration
```

## 🚀 Running the Market Analysis Agent

### Method 1: ADK Web Interface (Recommended)
```bash
adk web
```
Then navigate to `http://127.0.0.1:8000/dev-ui/` and select the market analysis agent.

### Method 2: Direct Access
Navigate directly to the market analysis agent:
```bash
# Navigate to http://127.0.0.1:8000/dev-ui/?app=interface_agent
```

### Method 3: Jupyter Notebook Testing
Use the provided Jupyter notebook for testing and experimentation:
```bash
cd adk-report-generator
jupyter notebook lol.ipynb
```

## 🏗️ Architecture Pattern

This repository demonstrates the **Agentic AI Design Pattern** with the following key concepts:

### 1. **Hierarchical Agent Structure**
- **Root Agent**: Main interface and coordinator
- **Sub-agents**: Specialized agents for specific tasks
- **Tool Integration**: Each agent has access to relevant tools

### 2. **Scalable Workflow Design**
- **Sequential Processing**: Agents work in coordinated sequences
- **Parallel Execution**: Multiple agents can work simultaneously
- **State Management**: Proper handling of conversation state and context

### 3. **Modular Components**
- **Agent Definitions**: Clear separation of agent responsibilities
- **Tool Libraries**: Reusable tools across different agents
- **Configuration Management**: Environment-based configuration

## 📊 Example: Market Analysis Workflow

The stock bot demonstrates a complete agentic workflow:

1. **User Input**: Stock symbol and date range
2. **Data Collection**: API agent fetches stock data
3. **News Analysis**: News agent gathers and analyzes market sentiment
4. **Technical Analysis**: Processing of price trends and indicators
5. **Report Generation**: Comprehensive analysis with recommendations

## 🔧 Development

### Extending the Market Analysis Agent
1. **Adding New Data Sources**: Create new sub-agents in `data_sub_agents/`
2. **Enhancing Analysis**: Modify the summarizer agent prompts and logic
3. **New Tools**: Add tools to the `api_agent/tools.py` for additional functionality
4. **Testing**: Use the Jupyter notebook for rapid prototyping and testing

### Agent Structure
- **Interface Agent**: Main coordinator that handles user input and orchestrates workflow
- **Sequential Agent**: Manages the execution flow between data retrieval and summarization
- **Sub-agents**: Specialized agents for specific tasks (API data, news analysis, summarization)

## 📝 Workshop Takeaways

This repository demonstrates:
- **Practical AI Implementation**: Real-world applications of AI agents
- **Scalable Architecture**: Patterns that work for complex workflows
- **Google Cloud Integration**: Leveraging Vertex AI and other GCP services
- **Best Practices**: Code organization, error handling, and user experience

## 🤝 Contributing

This repository serves as educational material from the workshop. Feel free to:
- Experiment with the market analysis agent
- Extend functionality by adding new data sources or analysis methods
- Improve the agent prompts and instructions
- Share improvements and learnings

## 📄 License

This project is provided as educational material from the Google Developer Group DevFest 2025 workshop.

## 🙋‍♂️ Support

For questions about the workshop content or implementation:
- Review the market analysis agent code and structure
- Check the ADK documentation
- Experiment with the provided Jupyter notebook
- Examine the agent prompts and tool implementations

---

**Workshop:** "It Starts with a Stock Bot: An Agentic AI Design Pattern for Scalable AI Workflows"  
**Event:** Google Developer Group DevFest 2025  
**Location:** Google HQ Dubai  
**Repository:** Practical examples and code from the workshop
