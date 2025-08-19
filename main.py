from product import Product
from store import Store

TITLE = "BEST BUY MENU"


def setup_store() -> Store:
    """
    Set up the initial store with default inventory.
    :return: Store object with initial product inventory
    """
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    return best_buy


def print_title():
    """
    Print the formatted title for the menu.
    """
    print()
    print(f"\t{TITLE.upper()}")
    print(f"\t{"_" * len(TITLE)}")


def start(store: Store):
    """
    Display the main menu and handle user input.
    :param store: Store object to operate on
    """
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
    """
    Display all active products in the store.
    :param store: Store object to list products from
    """
    product_list = store.get_all_products()

    seperator_line()

    for i, product in enumerate(product_list, 1):
        print(f"{i}. {product.show()}")

    seperator_line()


def show_total_amount(store: Store):
    """
    Display the total quantity of all items in the store.
    :param store: Store object to calculate total from
    """
    total = store.get_total_quantity()
    print(f"\nTotal of {total} items in store.")


def make_order(store: Store):
    """
    Handle the order process with user input validation.
    :param store: Store object to process order from
    """
    list_products(store)
    products = store.get_all_products()

    shopping_cart = []

    while True:

        while True:
            product_input = input(f"Which product do you want to order? (1 - {len(products)}) ")
            if not product_input.isnumeric() or 0 > int(product_input) or int(product_input) > len(products):
                print("Invalid input. Try again.")
                continue
            break

        while True:
            quantity_input = input(f"What amount do you want to order? ")
            if not quantity_input.isnumeric() or int(quantity_input) < 0:
                print("Invalid input. Try again.")
                continue
            break

        product_choice = products[int(product_input) - 1]
        quantity = int(quantity_input)

        shopping_cart.append((product_choice, quantity))

        if input("Would you like to add another item? (Y/N) ").lower() != "y":
            break
        print()

    seperator_line()
    try:
        total_price = store.order(shopping_cart)
        print(f"Order made. Your total price is ${total_price:.2f}.")
    except ValueError as e:
        print(f"Error with order: {e}")


def quit_program(store: Store):
    """
    Exit the program.
    :param store: Store object (not used but required for consistency)
    """
    quit()


def seperator_line():
    """
    Print a separator line for formatting.
    """
    print("-" * 15)


MENU_OPTIONS = {
    1: (list_products, "List all products in store"),
    2: (show_total_amount, "Show total amount in store"),
    3: (make_order, "Make an order"),
    4: (quit_program, "Quit")
    }


def main():
    """
    Main function to run the store application.
    """
    store = setup_store()

    while True:
        start(store)


if __name__ == "__main__":
    main()