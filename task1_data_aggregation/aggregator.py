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
from typing import Dict, List, Optional

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
        
        # missing or invalid data handling
        self.df = self._clean_data(self.df)
        
        return self.df
    
    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # remove rows with missing critical data
        df = df.dropna(subset=['company', 'year', 'revenue', 'profit'])
        
        # convert numeric columns
        df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
        df['profit'] = pd.to_numeric(df['profit'], errors='coerce')
        df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
        
        # remove rows with invalid numeric values
        df = df.dropna(subset=['revenue', 'profit', 'year'])
        
        return df
    
    def calculate_metrics(self, min_revenue: Optional[float] = None) -> List[Dict]:
        
        if self.df is None:
            self.load_data()
        
        # minimum revenue filter
        df = self.df.copy()
        if min_revenue is not None:
            df = df[df['revenue'] >= min_revenue]
            
        companies = df['company'].unique()
        results = []
        
        for company in companies:
            company_data = df[df['company'] == company].sort_values('year')
            
            metrics = {
                'company': company,
                'cui': company_data['cui'].iloc[0],
                'average_yearly_profit': self._calc_avg_profit(company_data),
                'yoy_revenue_growth': self._calc_yoy_growth(company_data),
                'profit_margin': self._calc_profit_margin(company_data),
                'period_years_analyzed': len(company_data)
            }

            results.append(metrics)
        
        return results
    
    def _calc_avg_profit(self, company_data: pd.DataFrame) -> float:
        return round(company_data['profit'].mean(), 2)
    
    def _calc_yoy_growth(self, company_data: pd.DataFrame) -> Optional[float]:
        if len(company_data) < 2:
            return None
        
        latest = company_data.iloc[-1]
        previous = company_data.iloc[-2]
        
        growth = ((latest['revenue'] - previous['revenue']) / previous['revenue']) * 100
        return round(growth, 2)
    
    def _calc_profit_margin(self, company_data: pd.DataFrame) -> float:
        latest = company_data.iloc[-1]
        margin = (latest['profit'] / latest['revenue']) * 100
        return round(margin, 2)
        
    def generate_report(self, min_revenue: Optional[float] = None, format: str = 'table') -> str:
        
        metrics = self.calculate_metrics(min_revenue)
        if format == 'json':
            return json.dumps(metrics, indent=2)
        
        report = "\n" + "=" * 80 + "\n"
        report += "FINANCIAL REPORT\n"
        report += "=" * 80 + "\n\n"
        
        if min_revenue:
            report += f"Filter: Minimum Revenue >= {min_revenue:,.2f}\n\n"
        
        for company in metrics:
            report += f"Company: {company['company']} (CUI: {company['cui']})\n"
            report += f"  Average Yearly Profit: {company['average_yearly_profit']:,.2f}\n"
            
            if company['yoy_revenue_growth'] is not None:
                report += f"  Year over year Revenue Growth: {company['yoy_revenue_growth']:+.2f}%\n"
            else:
                report += f"  Year over year Revenue Growth: N/A (insufficient data)\n"
            
            report += f"  Profit Margin: {company['profit_margin']:.2f}%\n"
            report += f"  Years Analyzed: {company['period_years_analyzed']}\n"
            report += "-" * 80 + "\n"
        
        return report
    
    
def main():
    
    import argparse
    
    parser = argparse.ArgumentParser(description='Financial Data Aggregation & Reporting')
    parser.add_argument('csv_file', help='Path to CSV file')
    parser.add_argument('--min-revenue', type=float, help='Minimum revenue filter')
    parser.add_argument('--format', choices=['table', 'json'], default='table',help='Output format')
    
    args = parser.parse_args()
    
    try:
        aggregator = FinancialAggregator(args.csv_file)
        aggregator.load_data()
        report = aggregator.generate_report(
            min_revenue=args.min_revenue,
            format=args.format
        )
        print(report)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
        