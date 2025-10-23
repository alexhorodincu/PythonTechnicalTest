""" Pydantic models """

from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class ReportCreate(BaseModel):
    title: str = Field(..., max_length=100, description="Report title")
    content: str = Field(..., max_length=2000, description="Report content")
    author: str = Field(..., min_length=1, description="Report author")
    
    @field_validator('title', 'author')
    @classmethod
    def not_empty(cls, v: str) -> str:
        #making sure fields not empty
        if not v.strip():
            raise ValueError("Field cannot be empty")
        return v.strip()
    
class Report(BaseModel):
    """Schema for complete report."""
    id: int
    title: str
    content: str
    author: str
    created_at: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Report",
                "content": "Report Content",
                "author": "Report Author",
                "created_at": "2025-10-23T11:40:00"
            }
        }


class ReportList(BaseModel):
    """Schema for list of reports."""
    total: int
    reports: list[Report]