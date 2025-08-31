from pydantic import BaseModel, Field

class ReportData(BaseModel):
    
    summary: str = Field(
        description="A brief summary of the report."
    )
    
    report_markdown: str = Field(
        description="The full report in markdown format."
    )
    
    follow_up_questions: list[str] = Field(
        description="A list of follow-up questions that could be explored further."
    )
    
    