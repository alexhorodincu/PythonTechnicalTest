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
    
    def test_empty_item_list(self):
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            InvoiceCalculator([])
            
    def test_invalid_tax_rate_too_high(self):
        items = [
            {"description": "Item", "quantity": 1, "unit_price": 100, "tax_rate": 1.5}
        ]
        
        with pytest.raises(ValueError, match="tax_rate must be between 0 and 1"):
            InvoiceCalculator(items)
    
    def test_invalid_tax_rate_negative(self):
        items = [
            {"description": "Item", "quantity": 1, "unit_price": 100, "tax_rate": -0.1}
        ]
        
        with pytest.raises(ValueError, match="tax_rate must be between 0 and 1"):
            InvoiceCalculator(items)