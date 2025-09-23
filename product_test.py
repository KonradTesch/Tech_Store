import pytest
from product import Product

def test_creating_product_valid():
    test_product =  Product(name="test", price=10, quantity=1)
    assert test_product.name == "test"
    assert test_product.price == 10
    assert test_product.quantity == 1


def test_creating_product_no_name():
    with pytest.raises(ValueError, match="Name cannot be an empty string"):
        Product(name="", price=10, quantity=1)

def test_creating_product_negative_price():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product(name="test", price=-10, quantity=1)


def test_creating_product_negative_quantity():
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        Product(name="test", price=10, quantity=-1)


def test_zero_quantity_inactive():
    test_product = Product(name="test", price=10, quantity=5)
    test_product.set_quantity(0)
    assert test_product.active == False


def test_buy_product_valid():
    test_product = Product(name="test", price=10, quantity=5)
    assert test_product.buy(2) == 20
    assert test_product.quantity == 3


def test_buy_product_too_much():
    test_product = Product(name="test", price=10, quantity=5)
    with pytest.raises(ValueError, match="test: Quantity is greater than what in store"):
        test_product.buy(20)