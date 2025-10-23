""" Invoice Calculator """

from typing import List, Dict

class InvoiceCalculator:
    
    def __init__(self, items: List[Dict]):
        if not items:
            raise ValueError("Items list cannot be empty")
        
        self.items = items
        self._validate_items()
        
    def _validate_items(self):
        required_fields = ['description', 'quantity', 'unit_price', 'tax_rate']
        
        for idx, item in enumerate(self.items):
            # check required fields
            missing = [f for f in required_fields if f not in item]
            if missing:
                raise ValueError(
                    f"Item {idx} missing required fields: {missing}"
                )
            
            # validate numeric values
            try:
                quantity = float(item['quantity'])
                unit_price = float(item['unit_price'])
                tax_rate = float(item['tax_rate'])
            except (TypeError, ValueError):
                raise ValueError(
                    f"Item {idx} has non-numeric quantity, unit_price, or tax_rate"
                )
            
            # validate ranges
            if quantity <= 0:
                raise ValueError(f"Item {idx} quantity must be positive")
            
            if unit_price < 0:
                raise ValueError(f"Item {idx} unit_price cannot be negative")
            
            if not (0 <= tax_rate <= 1):
                raise ValueError(
                    f"Item {idx} tax_rate must be between 0 and 1 (got {tax_rate})"
                )
    
    def calculate_subtotal(self) -> float:
        subtotal = sum(
            item['quantity'] * item['unit_price']
            for item in self.items
        )
        return round(subtotal, 2)
    
    def calculate_total_tax(self) -> float:
        total_tax = sum(
            item['quantity'] * item['unit_price'] * item['tax_rate']
            for item in self.items
        )
        return round(total_tax, 2)
    
    def calculate_grand_total(self) -> float:
        grand_total = self.calculate_subtotal() + self.calculate_total_tax()
        return round(grand_total, 2)

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
    
    calc = InvoiceCalculator(items)
    
    print("Invoice Calculator Demo")
    print("=" * 40)
    print(f"Subtotal: {calc.calculate_subtotal():.2f}")
    print(f"Total Tax: {calc.calculate_total_tax():.2f}")
    print(f"Grand Total: {calc.calculate_grand_total():.2f}")
    
if __name__ == "__main__":
    main()