import pytest
from decimal import Decimal
from ..models import Product
from ..service import InventoryService
from ..repository import InventoryRepository

@pytest.fixture
def service():
    """Create a fresh service instance for each test"""
    return InventoryService(InventoryRepository())

def test_add_product(service):
    """Test adding a new product"""
    service.add_product("Test", "Category", Decimal("10.00"), 5)
    product = service.repository.get("Test")
    assert product is not None
    assert product.name == "Test"
    assert product.price == Decimal("10.00")
    assert product.quantity == 5

def test_remove_product(service):
    """Test removing a product"""
    service.add_product("Test", "Category", Decimal("10.00"), 5)
    assert service.remove_product("Test") is True
    assert service.repository.get("Test") is None

def test_invalid_product_data(service):
    """Test validation of product data"""
    with pytest.raises(ValueError):
        service.add_product("", "Category", Decimal("10.00"), 5)  # empty name
    
    with pytest.raises(ValueError):
        service.add_product("Test", "", Decimal("10.00"), 5)  # empty category
    
    with pytest.raises(ValueError):
        service.add_product("Test", "Category", Decimal("-1.00"), 5)  # negative price