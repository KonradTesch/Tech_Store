from product import Product
from store import Store

TITLE = "BEST BUY MENU"
def setup_store() -> Store:
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)

    return best_buy


def print_title():
    print()
    print(f"\t{TITLE.upper()}")
    print(f"\t{"_" * len(TITLE)}")


def start(store:Store):
    print_title()

    for index, (function, label) in MENU_OPTIONS.items():
        print(f"{index}. {label}")

    print()

    while True:
        menu_input = input(f"Enter your choice (1 - {len(MENU_OPTIONS)}): ")
        if not menu_input.isnumeric() or not MENU_OPTIONS.get(int(menu_input)):
            print("Invalid input. Try again.")
            continue
        function = MENU_OPTIONS[int(menu_input)][0]
        function(store)
        input("Press ENTER to continue...")
        break


def list_products(store: Store):
    product_list = store.get_all_products()

    seperator_line()

    for i, product in enumerate(product_list, 1):
        print(f"{i}. {product.show()}")

    seperator_line()


def show_total_amount(store: Store):
    total = store.get_total_quantity()

    print(f"\nTotal of {total} items in store.")


def make_order(store: Store):
    list_products(store)
    products = store.get_all_products()

    shopping_card = []

    while True:

        while True:
            product_input = input(f"Which product do you want to order? (1 - {len(products)}) ")
            if not product_input.isnumeric() or 0 > int(product_input) or int(product_input) > len(products):
                print("Invalid input. Try again.")
                continue
            break

        while True:
            quantity_input = input(f"What amount do you want to order? ")
            if not quantity_input.isnumeric() and int(product_input) < 0:
                print("Invalid input. Try again.")
                continue
            break

        product_choice = products[int(product_input) - 1]
        quantity = int(quantity_input)

        shopping_card.append((product_choice, quantity))

        if input("Would you like to add another item? (Y/N) ").lower() != "y":
            break
        print()

    seperator_line()
    total_price = store.order(shopping_card)
    print(f"Order made. Your total price is ${total_price:.2f}.")



def quit_program(store: Store):
    quit()


def seperator_line():
    print("-" * 15)


MENU_OPTIONS = {
    1: (list_products, "List all products in store"),
    2: (show_total_amount, "Show total amount in store"),
    3: (make_order, "Make an order"),
    4: (quit_program, "Quit")
    }

def main():
    store = setup_store()

    while True:
        start(store)


if __name__ == '__main__':
    main()