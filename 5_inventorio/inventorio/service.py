from decimal import Decimal
from typing import List, Optional
from .models import Product
from .repository import InventoryRepository

class InventoryService:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def add_product(self, name: str, category: str, price: Decimal, quantity: int) -> None:
        if not name or not category:
            raise ValueError("Nome e categoria são obrigatórios")
        if price <= 0:
            raise ValueError("Preço deve ser maior que zero")
        if quantity < 0:
            raise ValueError("Quantidade não pode ser negativa")

        product = Product(name=name, category=category, price=price, quantity=quantity)
        self.repository.add(product)

    def update_quantity(self, name: str, quantity_change: int) -> None:
        product = self.repository.get(name)
        if not product:
            raise ValueError(f"Produto '{name}' não encontrado")
        
        new_quantity = product.quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Quantidade resultante não pode ser negativa")
        
        product.quantity = new_quantity
        self.repository.add(product)

    def remove_product(self, name: str) -> bool:
        return self.repository.remove(name)

    def get_by_category(self, category: str) -> List[Product]:
        return [p for p in self.repository.get_all().values() 
                if p.category.lower() == category.lower()]

    def get_most_expensive(self) -> Optional[Product]:
        products = list(self.repository.get_all().values())
        return max(products, key=lambda p: p.price) if products else None

    def get_below_stock(self, minimum: int) -> List[Product]:
        return [p for p in self.repository.get_all().values() 
                if p.quantity < minimum]