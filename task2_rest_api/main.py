""" FastAPI app """

from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from task2_rest_api.models import Report, ReportCreate, ReportList
from task2_rest_api.database import db

app = FastAPI(
    title="Report Manager API",
    description="Simple REST API for managing reports",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint with API information."""
    return {
        "message": "Report Manager API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.post("/reports", response_model=Report, status_code=201, tags=["Reports"])
def create_report(report: ReportCreate):
    new_report = db.create_report(report)
    return new_report

@app.get("/reports", response_model=ReportList, tags=["Reports"])
def list_reports(
    sort: Optional[str] = Query(
        None, 
        description="Sort by field: 'created_at' or 'title'"
    )
):
    """
    Get all reports.
    
    Args:
        sort: Optional sorting parameter
        
    Returns:
        List of all reports
    """
    # validate sort parameter
    if sort and sort not in ['created_at', 'title']:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort parameter. Use 'created_at' or 'title'"
        )
    
    reports = db.get_all_reports(sort_by=sort)
    return ReportList(total=len(reports), reports=reports)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)