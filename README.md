# Deep Research

Deep Research is an AI-powered research assistant that automates the process of planning, searching, synthesizing, and reporting on any research topic. It features a modular agent-based architecture and a user-friendly Gradio interface.

## Features

- **Automated Research Workflow**: Plans web searches, executes them, synthesizes findings, writes a detailed markdown report, and sends results via email.
- **Agent-Based Design**: Specialized agents for planning, searching, writing, and emailing.
- **Gradio UI**: Simple web interface for entering research queries and viewing results.

## How It Works

1. **User submits a research query** via the Gradio interface.
2. **Planner Agent** generates a set of web searches to answer the query.
3. **Search Agent** performs each search and summarizes the results.
4. **Writer Agent** synthesizes the findings into a detailed markdown report.

## File Overview

- `deep_research.py`: Main entry point and Gradio UI.
- `research_manager.py`: Orchestrates the research workflow.
- `planner_agent.py`: Plans web searches for a given query.
- `search_agent.py`: Executes web searches and summarizes results.
- `writer_agent.py`: Synthesizes findings into a markdown report.

## Requirements

- Python 3.8+
- Gradio
- python-dotenv
- sendgrid
- pydantic

## Setup

1. **Install dependencies**:
   ```bash
   pip install gradio python-dotenv sendgrid pydantic
   ```
2. **Set environment variables**:
   - Create a `.env` file with your SendGrid API key:
     ```
     SENDGRID_API_KEY=your_sendgrid_api_key
     ```

## Usage

Run the app:
```bash
python deep_research.py
```
The Gradio UI will open in your browser. Enter a topic to start the research process.

## Customization

- Adjust the number of searches in `planner_agent.py` (`HOW_MANY_SEARCHES`).

## License

MIT
