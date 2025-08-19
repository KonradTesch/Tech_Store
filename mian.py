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
        break


def list_products(store: Store):
    pass


def show_total_amount(store: Store):
    pass


def make_order(store: Store):
    pass


def quit_program(store: Store):
    quit()


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