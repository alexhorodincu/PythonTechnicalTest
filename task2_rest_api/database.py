""" in-memory storage """

from datetime import datetime
from typing import Dict, List, Optional
from task2_rest_api.models import Report, ReportCreate


class InMemoryDB:
    """in-memory database for reports"""
    
    def __init__(self):
        # empty data base initialization
        self._reports: Dict[int, Report] = {}
        self._next_id: int = 1
    
    def create_report(self, report_data: ReportCreate) -> Report:
        """
        Create a new report.
        
        Args:
            report_data: Report creation data
            
        Returns:
            Created report with ID
        """
        report = Report(
            id=self._next_id,
            title=report_data.title,
            content=report_data.content,
            author=report_data.author,
            created_at=datetime.now()
        )
        
        self._reports[self._next_id] = report
        self._next_id += 1
        
        return report
    
db = InMemoryDB()