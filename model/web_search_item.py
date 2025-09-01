from pydantic import BaseModel, Field

class WebSearchItem(BaseModel):
    
    reason: str = Field(description="The reason why this query is needed.")
    
    query: str = Field(description="The search query to use.")