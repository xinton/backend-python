from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Product:
    name: str
    category: str
    price: Decimal
    quantity: int

    def __post_init__(self):
        self.price = Decimal(str(self.price))