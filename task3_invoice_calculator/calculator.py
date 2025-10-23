""" Invoice Calculator """

from typing import List, Dict

class InvoiceCalculator:
    
    def __init__(self, items: List[Dict]):
        if not items:
            raise ValueError("Items list cannot be empty")
        
        self.items = items

def main():
    items = [
        {
            "description": "Laptop",
            "quantity": 2,
            "unit_price": 3000,
            "tax_rate": 0.19
        },
        {
            "description": "Mouse",
            "quantity": 5,
            "unit_price": 100,
            "tax_rate": 0.19
        }
    ]
    
    #calc = InvoiceCalculator(items)
    
if __name__ == "__main__":
    main()