import json
from decimal import Decimal
from typing import Dict, Optional
from .models import Product

class InventoryRepository:
    def __init__(self, filename: str = "inventory.json"):
        self.filename = filename
        self.inventory: Dict[str, Product] = {}
        self.load()
    
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.inventory = {
                    name: Product(
                        name=name,
                        category=info['category'],
                        price=Decimal(str(info['price'])),
                        quantity=info['quantity']
                    ) for name, info in data.items()
                }
        except FileNotFoundError:
            self.inventory = {}

    def save(self):
        data = {
            name: {
                'category': product.category,
                'price': str(product.price),
                'quantity': product.quantity
            } for name, product in self.inventory.items()
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def add(self, product: Product) -> None:
        self.inventory[product.name] = product
        self.save()

    def remove(self, name: str) -> bool:
        if name in self.inventory:
            del self.inventory[name]
            self.save()
            return True
        return False

    def get(self, name: str) -> Optional[Product]:
        return self.inventory.get(name)

    def get_all(self) -> Dict[str, Product]:
        return self.inventory.copy()