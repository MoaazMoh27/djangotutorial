"""
type_hints_example.py
----------------------
Demonstrates Python type hints using a small "add a product to cart"
program. Every input() call has a clear message telling the user
exactly what to type before they type it.

NOTE: type hints here are just labels -- Python does NOT enforce them
at runtime. That's why each input is still manually validated with a
loop below. (Pydantic, in the other file, is what actually enforces
these rules automatically.)
"""


def get_product_name() -> str:
    """Ask the user for a product name. Any text is accepted."""
    print("\nEnter the name of the product (e.g. 'Apple', 'Notebook'):")
    name = input("> ")
    return name


def get_product_price() -> float:
    """Ask the user for a price. Loops until a valid decimal number is entered."""
    while True:
        print("\nEnter the price of the product in dollars (e.g. 2.50):")
        raw_price = input("> ")
        try:
            price = float(raw_price)
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            return price
        except ValueError:
            print(f"'{raw_price}' is not a valid number. Try again.")


def get_product_quantity() -> int:
    """Ask the user for a quantity. Loops until a valid whole number (1-99) is entered."""
    while True:
        print("\nEnter how many units the customer wants (a whole number from 1 to 99):")
        raw_quantity = input("> ")
        try:
            quantity = int(raw_quantity)
            if quantity < 1 or quantity > 99:
                print("Quantity must be between 1 and 99. Try again.")
                continue
            return quantity
        except ValueError:
            print(f"'{raw_quantity}' is not a whole number. Try again.")


def get_wants_receipt() -> bool:
    """Ask a yes/no question and convert it to a real bool."""
    while True:
        print("\nDo you want to print a receipt? (type 'y' for yes or 'n' for no):")
        answer = input("> ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please type exactly 'y' or 'n'.")


def calculate_total(price: float, quantity: int) -> float:
    """Pure calculation -- no input here, just math with typed values."""
    return price * quantity


def display_receipt(name: str, price: float, quantity: int, total: float) -> None:
    """Prints a formatted summary. Returns nothing (-> None)."""
    print("\n----- RECEIPT -----")
    print(f"Product:  {name}")
    print(f"Price:    ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total:    ${total:.2f}")
    print("--------------------")


def main() -> None:
    print("=== Add a Product (Type Hints Example) ===")

    name: str = get_product_name()
    price: float = get_product_price()
    quantity: int = get_product_quantity()
    wants_receipt: bool = get_wants_receipt()

    total: float = calculate_total(price, quantity)

    if wants_receipt:
        display_receipt(name, price, quantity, total)
    else:
        print(f"\nTotal for {quantity}x {name}: ${total:.2f}")


if __name__ == "__main__":
    main()