from pydantic import BaseModel, Field
from model.web_search_item import WebSearchItem

class WebSearchPlan(BaseModel):
    
    searches: list[WebSearchItem] = Field(
        description="A list of web search items to be performed."
    )