class Product:
    """
    Represents a product in the store with name, price, quantity and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new product.
        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Available quantity in stock
        """
        if not isinstance(name, str) and name != "":
            raise TypeError("Name must be a non-empty string")

        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price
        self.quantity = self._validate_quantity(quantity)
        self.active = quantity > 0

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.
        :return: Current quantity as integer
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set a new quantity for the product and update active status.
        :param quantity: New quantity to set
        """
        self.quantity = self._validate_quantity(quantity)
        self.active = quantity > 0

    def is_active(self) -> bool:
        """
        Check if the product is currently active.
        :return: True if product is active, False otherwise
        """
        return self.active

    def activate(self):
        """
        Manually activate the product.
        """
        self.active = True

    def deactivate(self):
        """
        Manually deactivate the product.
        """
        self.active = False

    def show(self):
        """
        Get a formatted string representation of the product.
        :return: Formatted string with name, price, and quantity
        """
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Purchase a specified quantity of the product.
        :param quantity: Amount to purchase
        :return: Total cost for the purchase
        """
        if self._validate_quantity(quantity) and quantity > self.quantity:
            raise ValueError(f"{self.name}: Quantity is greater than what in store")

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price

    @staticmethod
    def _validate_quantity(quantity) -> int:
        """
        Validate the quantity type and value.
        :param quantity: The quantity to validate
        :return: The validated quantity
        """
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity should be a number.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        return quantity