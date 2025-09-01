from agents import Agent
from model.web_search_plan import WebSearchPlan


NUM_OF_SEARCH = 3

INSTRUCTIONS = f"You are a helpful research assistant. Given a query, come up with a set of web searches \
to perform to best answer the query. Output {NUM_OF_SEARCH} terms to query for."

planner_agent = Agent(
    name="Planner Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)