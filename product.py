class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        self.active = quantity > 0


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price:.2f}$, Quantity: {self.quantity}")


    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Quantity is greater than product quantity")

        self.set_quantity(self.quantity - quantity)
        return  quantity * self.price

