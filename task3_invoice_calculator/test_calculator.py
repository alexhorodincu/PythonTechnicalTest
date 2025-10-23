""" 
Unit tests for Invoice Calculator

"""

import pytest
from task3_invoice_calculator.calculator import InvoiceCalculator

class TestInvoiceCalculator:
    
    def test_normal_case(self):
        items = [
            {"description": "Laptop", "quantity": 2, "unit_price": 3000, "tax_rate": 0.19},
            {"description": "Mouse", "quantity": 5, "unit_price": 100, "tax_rate": 0.19}
        ]

        calc = InvoiceCalculator(items)
        
        assert calc.calculate_subtotal() == 6500.0
        assert calc.calculate_total_tax() == 1235.0
        assert calc.calculate_grand_total() == 7735.0