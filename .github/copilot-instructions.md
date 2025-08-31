# Copilot Instructions for Deep Research Project

## Project Overview
Deep Research is an AI-powered research assistant that automates comprehensive research workflows using a modular agent-based architecture with a Gradio web interface.

## Architecture & Design Patterns

### Agent-Based System
- **Planner Agent** (`planner_agent.py`): Generates strategic web search plans
- **Search Agent** (`search_agent.py`): Executes searches and summarizes results
- **Writer Agent** (`writer_agent.py`): Synthesizes findings into markdown reports
- **Research Manager** (`research_manager.py`): Orchestrates the entire workflow

### Key Design Principles
- Modular agent separation of concerns
- Async/await patterns for concurrent operations
- Pydantic models for data validation
- Environment-based configuration
- Error handling and graceful degradation

## Code Style & Conventions

### Python Standards
- Follow PEP 8 style guidelines
- Use type hints for all function parameters and returns
- Prefer descriptive variable names (e.g., `research_query` over `q`)
- Use docstrings for all classes and functions

### Agent Implementation Patterns
```python
class AgentName:
    def __init__(self, config: Config):
        self.config = config
    
    async def execute(self, input_data: InputModel) -> OutputModel:
        """Execute the agent's primary function."""
        pass
```

### Error Handling
- Use try/except blocks for external API calls
- Log errors with appropriate context
- Return meaningful error messages to users
- Implement retry logic for network operations

## Dependencies & Libraries

### Core Dependencies
- **Gradio**: Web UI framework - prefer simple interfaces over complex layouts
- **python-dotenv**: Environment management - always load from `.env`
- **sendgrid**: Email functionality - handle API errors gracefully
- **pydantic**: Data validation - use for all data models

### Suggested Additions
When adding new features, consider:
- `asyncio` for concurrent operations
- `logging` for better debugging
- `requests` with retry logic for web APIs
- `beautifulsoup4` for web scraping enhancements

## File Structure Guidelines

### New Agent Creation
When creating new agents:
1. Create `{agent_name}_agent.py` in root directory
2. Follow the established agent interface pattern
3. Add configuration options to main config
4. Update `research_manager.py` workflow
5. Add tests in `tests/` directory (create if needed)

### Configuration Management
- Store all API keys in `.env` file
- Use environment variables for configurable parameters
- Create configuration classes using Pydantic
- Provide sensible defaults for optional settings

## UI Development with Gradio

### Interface Patterns
- Keep interfaces simple and intuitive
- Use progress indicators for long-running operations
- Provide clear error messages to users
- Support both text input and file uploads where appropriate

### Example Gradio Component Usage
```python
with gr.Blocks() as interface:
    research_input = gr.Textbox(label="Research Query")
    submit_btn = gr.Button("Start Research")
    results_output = gr.Markdown()
```

## API Integration Best Practices

### External API Calls
- Always implement rate limiting
- Use exponential backoff for retries
- Validate API responses before processing
- Cache results when appropriate
- Handle API quota/limit errors gracefully

### Search and Data Processing
- Sanitize and validate all user inputs
- Implement result deduplication
- Use structured data models for search results
- Provide fallback options when APIs fail

## Testing Guidelines

### Unit Tests
- Test each agent independently
- Mock external API calls
- Test error conditions and edge cases
- Validate data model constraints

### Integration Tests
- Test the complete research workflow
- Test UI interactions
- Test email delivery functionality
- Test with various input formats

## Environment Setup

### Required Environment Variables
```bash
SENDGRID_API_KEY=your_sendgrid_api_key
# Add other API keys as needed
RESEARCH_TIMEOUT=300  # seconds
MAX_SEARCHES=10
```

### Development Environment
- Use virtual environments for dependency isolation
- Pin dependency versions in requirements.txt
- Set up pre-commit hooks for code quality
- Use environment-specific .env files

## Common Patterns & Utilities

### Async Operations
Prefer async/await for I/O operations:
```python
async def perform_search(query: str) -> SearchResult:
    async with aiohttp.ClientSession() as session:
        # Implementation
```

### Data Validation
Use Pydantic for all data structures:
```python
class ResearchQuery(BaseModel):
    topic: str
    max_searches: int = 5
    include_citations: bool = True
```

### Logging
Implement structured logging:
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Starting research", extra={"query": query})
```

## Performance Considerations

- Implement caching for repeated searches
- Use connection pooling for HTTP requests
- Process searches concurrently when possible
- Optimize report generation for large datasets
- Monitor memory usage during large research tasks

## Security Guidelines

- Validate all user inputs to prevent injection attacks
- Use secure methods for API key storage
- Implement rate limiting to prevent abuse
- Sanitize outputs to prevent XSS in web interface
- Use HTTPS for all external API communications

## Feature Extension Ideas

When adding new features, consider:
- Multi-language research support
- Advanced filtering and search operators
- Integration with academic databases
- Collaborative research features
- Export options (PDF, DOCX, etc.)
- Research project management
- Citation management and formatting
