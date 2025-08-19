from Tech_Store.product import Product

class Store:
    def __init__(self, product_list: list):
        self.product_list = product_list


    def add_product(self, product):
        self.product_list.append(product)


    def remove_product(self, product):
        if product not in self.product_list:
            raise ValueError('Product not found')
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        total = 0
        for product in self.product_list:
            total += product.quantity

        return total


    def get_all_products(self) -> list[Product]:
        active_products = [product for product in self.product_list if product.is_active()]
        return active_products


    def order(self, shopping_cart: list[tuple]):
        total_price = 0
        for product, quantity in shopping_cart:
            if product not in self.product_list:
                raise ValueError(f'Product {product.name} not in store')

            index = self.product_list.index(product)
            total_price += self.product_list[index].buy(quantity)

        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                   ]

    best_buy = Store(product_list)
