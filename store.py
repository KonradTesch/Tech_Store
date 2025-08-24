from product import Product

class Store:
    """
    Represents a store that manages a collection of products.
    """

    def __init__(self, product_list: list):
        """
        Initialize a new store with a list of products.
        :param product_list: List of Product objects
        """
        self.product_list = []
        for product in product_list:
            self.product_list.append(self._validate_product(product))



    def add_product(self, product):
        """
        Add a new product to the store.
        :param product: Product object to add
        """
        self.product_list.append(self._validate_product(product))

    def remove_product(self, product):
        """
        Remove a product from the store.
        :param product: Product object to remove
        """
        if product not in self.product_list:
            raise ValueError("Product not found")
        self.product_list.remove(self._validate_product(product))

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.
        :return: Total quantity as integer
        """
        total = 0
        for product in self.product_list:
            total += product.quantity
        return total

    def get_all_products(self) -> list[Product]:
        """
        Get all active products in the store.
        :return: List of active Product objects
        """
        active_products = [product for product in self.product_list if product.is_active()]
        return active_products

    def order(self, shopping_cart: list[tuple]):
        """
        Process an order with multiple products and quantities.
        :param shopping_cart: List of tuples containing (product, quantity)
        :return: Total price for the entire order
        """
        total_price = 0
        for product, quantity in shopping_cart:
            if product not in self.product_list:
                raise ValueError(f"Product {product.name} not in store")

            index = self.product_list.index(product)
            total_price += self.product_list[index].buy(quantity)

        return total_price

    @staticmethod
    def _validate_product(product) -> Product:
        """
        Validate a product object.
        :param product: The product to validate
        :return: The validated product
        """
        if not isinstance(product, Product):
            raise TypeError(f"Product {product.name} must be of type Product")

        return product