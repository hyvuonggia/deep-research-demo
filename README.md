---
title: deep-research-demo
app_file: deep_research.py
sdk: gradio
sdk_version: 5.44.1
---
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

## Usage


Run the app locally:
```bash
python deep_research.py
```
The Gradio UI will open in your browser. Enter a topic to start the research process.

Or use the deployed app here:
[https://huggingface.co/spaces/hyvuonggia/deep-research-demo](https://huggingface.co/spaces/hyvuonggia/deep-research-demo)

## Customization

- Adjust the number of searches in `planner_agent.py` (`HOW_MANY_SEARCHES`).

## License

MIT
