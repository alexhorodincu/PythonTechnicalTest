# Python Technical Test - Tasks 1, 2, 3

## Overview
This repository contains implementations for three tasks:
1. **Data Aggregation & Reporting** - Financial data analysis
2. **REST API** - Report manager with FastAPI
3. **Invoice Calculator** - TDD with unit tests

## Requirements
- Python >= 3.11
- Use Git
- PEP8 style

## Installation
```bash
# Clone repository
git clone git@github.com:alexhorodincu/PythonTechnicalTest.git
cd PythonTechnicalTest

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Task 1: Data Aggregation
```bash
# Run with sample data
python -m task1_data_aggregation.aggregator data/financial.csv

# With minimum revenue filter
python -m task1_data_aggregation.aggregator data/financial.csv --min-revenue 100000

# JSON output
python -m task1_data_aggregation.aggregator data/financial.csv --format json
```

### Task 2: REST API
```bash
# Start the API server
uvicorn task2_rest_api.main:app --reload

# API will be available at: http://localhost:8000
# OpenAPI docs at: http://localhost:8000/docs
```

**API Endpoints:**
- `POST /reports` - Create report
- `GET /reports` - List all reports
- `GET /reports/{id}` - Get specific report
- `DELETE /reports/{id}` - Delete specific report
- `GET /reports?sort=created_at` - List with sorting

### Task 3: Invoice Calculator
```bash
# Run example
python -m task3_invoice_calculator.calculator

# Run tests
pytest task3_invoice_calculator/test_calculator.py -v

# Run tests with coverage
pytest task3_invoice_calculator/test_calculator.py --cov=task3_invoice_calculator --cov-report=html
```

## Project Structure


PythonTechnicalTest/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── financial.csv           # Sample data for Task 1
│
├── task1_data_aggregation/     # Task 1: Financial aggregation
│   ├── __init__.py
│   ├── aggregator.py  
│         
├── task2_rest_api/             # Task 2: FastAPI application
│   ├── __init__.py
│   ├── main.py                 # FastAPI app
│   ├── models.py               # Pydantic models
│   └── database.py             # In-memory storage
│
├── task3_invoice_calculator/   # Task 3: Invoice calculator + tests
│   ├── __init__.py
│   ├── calculator.py           # InvoiceCalculator class
│   └── test_calculator.py      # Pytest tests
└── 


## Design Decisions

### Task 1 - Data Aggregation
- **Pandas**: Chosen for robust CSV handling and data manipulation. 
Built-in csv module would be also fine for keeping things simple.
- **Modular design**: Separate methods for each calculation
- **Error handling**: Graceful handling of missing/invalid data
- **CLI support**: argparse for command-line usage

### Task 2 - REST API
- **FastAPI**: Modern, fast, automatic OpenAPI docs
- **In-memory storage**: Simple Dict-based storage for this scope
- **Pydantic validation**: Automatic request/response validation
- **Proper HTTP codes**: 201, 204, 404 as appropriate

### Task 3 - Invoice Calculator
- **TDD approach**: Tests written to guide implementation
- **Data validation tests**: All edge cases covered
- **Rounding**: Proper floating-point rounding to 2 decimals
- **pytest**: Industry-standard testing framework

## Testing

Tests can also be run in Visual Studio Code

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov --cov-report=html
```

## Author
Alexandru Horodincu
