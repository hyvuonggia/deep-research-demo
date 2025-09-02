

import asyncio
from agents import Runner, gen_trace_id, trace
from model.report_data import ReportData
from model.web_search_item import WebSearchItem
from model.web_search_plan import WebSearchPlan
from planner_agent import planner_agent
from search_agent import search_agent
from writer_agent import writer_agent

class ResearchManager:

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """Plan a set of web searches to perform given a query."""
        print(f"Planning searches for query: {query}")
        result = await Runner.run(
            planner_agent,
            input=query,
        )
        print(f"Search plan generated: {result}")
        return result.final_output_as(WebSearchPlan)
    

    async def search(self, item: WebSearchItem) -> str:
        print(f"Starting search for item: {item}")
        input = f"Search the web for '{item.query}', Reason for searching: {item.reason} "
        result = await Runner.run(
            search_agent,
            input,
        )
        print(f"Search result for '{item.query}': {result}")
        return result.final_output
    
    
    async def perform_searches(self, plan: WebSearchPlan) -> list[str]:
        """Perform a set of web searches given a plan."""
        print(f"Performing searches for plan: {plan}")
        results = []
        tasks = [asyncio.create_task(self.search(item)) for item in plan.searches]
        for task in asyncio.as_completed(tasks):
            result = await task
            print(f"Search completed with result: {result}")
            results.append(result)
        print(f"All searches completed. Total results: {len(results)}")
        return results
    
    
    async def write_report(self, query: str, search_results: list[str]) -> ReportData:
        """Generate a research report using the writer_agent."""
        input_text = f"Research Query: {query}\n\nSearch Results:\n" + "\n\n".join([f"Result {i+1}: {result}" for i, result in enumerate(search_results)])
        print("Step 3: Writing report...")
        report = await Runner.run(
            writer_agent,
            input=input_text,
        )
        print(f"Report generated: {report}")
        return report.final_output_as(ReportData)
   
   
    async def run(self, query: str):
        """ Run the deep research process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting research...")
            search_plan = await self.plan_searches(query)
            yield "Searches planned, starting to search..."     
            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report..."
            report = await self.write_report(query, search_results)
            yield report.report_markdown

   