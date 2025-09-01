

import asyncio
from agents import Runner
from model.web_search_item import WebSearchItem
from model.web_search_plan import WebSearchPlan
import planner_agent
import search_agent

class ResearchManager:

    async def plan_searchs(self, query: str) -> WebSearchPlan:
        """Plan a set of web searches to perform given a query."""
        print(f"Planning searches for query: {query}")
        result = await Runner.run(
            planner_agent,
            input={"query": query},
        )
        print(f"Search plan generated: {result}")
        return result
    

    async def search(self, item: WebSearchItem) -> str:
        print(f"Starting search for item: {item}")
        input = f"Search the web for '{item.query}', Reason for searching: {item.reason} "
        result = await Runner.run(
            search_agent,
            input,
        )
        print(f"Search result for '{item.query}': {result}")
        return result
    
    
    async def perform_searches(self, plan: WebSearchPlan) -> list[str]:
        """Perform a set of web searches given a plan."""
        print(f"Performing searches for plan: {plan}")
        results = []
        tasks = [asyncio.create_task(self.search(item)) for item in plan.searchs]
        for task in asyncio.as_completed(tasks):
            result = await task
            print(f"Search completed with result: {result}")
            results.append(result)
        print(f"All searches completed. Total results: {len(results)}")
        return results
    
    
    async def write_report(self, query: str, search_results: list[str]):
        """Generate a research report using the writer_agent."""
        from writer_agent import writer_agent
        input_data = {
            "query": query,
            "search_results": search_results
        }
        print("Step 3: Writing report...")
        report = await Runner.run(
            writer_agent,
            input=input_data,
        )
        print(f"Report generated: {report}")
        return report
    
    
    async def run(self, query: str):
        """Run the full research workflow, yielding after each step."""
        # Step 1: Plan searches
        print("Step 1: Planning searches...")
        plan = await self.plan_searchs(query)
        yield {"step": "plan_searchs", "result": plan}

        # Step 2: Perform searches
        print("Step 2: Performing searches...")
        search_results = await self.perform_searches(plan)
        yield {"step": "perform_searches", "result": search_results}

        # Step 3: Write report
        report = await self.write_report(query, search_results)
        yield {"step": "write_report", "result": report}

    