"""
Implement a small app that reads a CSV of company financials and
produces a summary report.

Requirements
- Load the CSV (use pandas or the built-in csv module).
- Compute for each company:
- average yearly profit
- year-over-year revenue growth (latest year vs previous)
- profit margin (%) for the latest year.
- Print or return a formatted summary (e.g., table or JSON).
- Handle missing/invalid data gracefully.
- Allow filtering by minimum revenue (e.g., via CLI arg or function
parameter).
"""

import pandas as pd
from pathlib import Path
import json

class FinancialAggregator:
    
    def __init__(self, csv_path: str):
        """
        Aggregator initialize with CSV file path.
        
        Args:
            csv_path: Path to the input csv file
        """
        self.csv_path = Path(csv_path)
        self.df = None
        
    def load_data(self) -> pd.DataFrame:
        
        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
        
        self.df = pd.read_csv(self.csv_path)
        
        required_cols = ['company', 'cui', 'year', 'revenue', 'profit']
        missing_cols = set(required_cols) - set(self.df.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        return self.df
    
def main():
    
    import argparse
    
    parser = argparse.ArgumentParser(description='Financial Data Aggregation & Reporting')
    parser.add_argument('csv_file', help='Path to CSV file')
    
    args = parser.parse_args()
    
    try:
        aggregator = FinancialAggregator(args.csv_file)
        aggregator.load_data()
        print(aggregator.df)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
        