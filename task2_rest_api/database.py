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
    
    def get_all_reports(self, sort_by: Optional[str] = None) -> List[Report]:
        """
        Get all reports, optionally sorted.
        
        Args:
            sort_by: Field to sort by ('created_at' or 'title')
            
        Returns:
            List of reports
        """
        reports = list(self._reports.values())
        
        if sort_by == 'created_at':
            reports.sort(key=lambda r: r.created_at)
        elif sort_by == 'title':
            reports.sort(key=lambda r: r.title.lower())
        
        return reports
    
    def get_report(self, report_id: int) -> Optional[Report]:
        """
        Get a report by ID.
        
        Args:
            report_id: Report ID
            
        Returns:
            Report or None if not found
        """
        return self._reports.get(report_id)
    
    def delete_report(self, report_id: int) -> bool:
        """
        Delete a report.
        
        Args:
            report_id: Report ID to delete
            
        Returns:
            True if deleted, False if not found
        """
        if report_id in self._reports:
            del self._reports[report_id]
            return True
        return False
    
db = InMemoryDB()