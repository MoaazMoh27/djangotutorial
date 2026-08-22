"""
pydantic_example.py
---------------------
Demonstrates Pydantic v2 using the same "add a product to cart" idea
as type_hints_example.py, but validation is handled AUTOMATICALLY by
the Product model instead of manual if-checks.

Every input() call has a clear message telling the user exactly what
to type before they type it.

Requires:
    py -m pip install pydantic
"""

from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    """
    Defines what a valid product looks like.
    Pydantic enforces these rules automatically when we build a Product.
    """
    name: str
    price: float = Field(gt=0)          # must be strictly greater than 0
    quantity: int = Field(ge=1, le=99)  # must be between 1 and 99


def get_product_name() -> str:
    print("\nEnter the name of the product (e.g. 'Apple', 'Notebook'):")
    return input("> ")


def get_product_price_raw() -> str:
    print("\nEnter the price of the product in dollars (e.g. 2.50):")
    print("(must be a number greater than 0)")
    return input("> ")


def get_product_quantity_raw() -> str:
    print("\nEnter how many units the customer wants:")
    print("(must be a whole number from 1 to 99)")
    return input("> ")


def get_wants_receipt() -> bool:
    while True:
        print("\nDo you want to print a receipt? (type 'y' for yes or 'n' for no):")
        answer = input("> ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please type exactly 'y' or 'n'.")


def build_valid_product() -> Product:
    """
    Keeps asking for name/price/quantity until Pydantic accepts them.
    Notice there is NO manual "if price < 0" check here -- the Product
    model itself is what enforces the rules.
    """
    while True:
        name = get_product_name()
        raw_price = get_product_price_raw()
        raw_quantity = get_product_quantity_raw()

        try:
            # Convert the raw text to the types expected by the model before
            # constructing it. This satisfies static type checkers while still
            # letting Pydantic validate the values and enforce the field rules.
            price = float(raw_price)
            quantity = int(raw_quantity)
            product = Product(name=name, price=price, quantity=quantity)
            return product
        except (ValidationError, ValueError) as e:
            if isinstance(e, ValidationError):
                print("\nThat product was rejected. Here's why:")
                for error in e.errors():
                    field = error["loc"][0]
                    message = error["msg"]
                    print(f"  - {field}: {message}")
            else:
                print("\nPlease enter a valid number for price and quantity.")
            print("Let's try again.")


def display_receipt(product: Product) -> None:
    total = product.price * product.quantity
    print("\n----- RECEIPT -----")
    print(f"Product:  {product.name}")
    print(f"Price:    ${product.price:.2f}")
    print(f"Quantity: {product.quantity}")
    print(f"Total:    ${total:.2f}")
    print("--------------------")


def main() -> None:
    print("=== Add a Product (Pydantic Example) ===")

    product = build_valid_product()
    wants_receipt = get_wants_receipt()

    if wants_receipt:
        display_receipt(product)
    else:
        total = product.price * product.quantity
        print(f"\nTotal for {product.quantity}x {product.name}: ${total:.2f}")


if __name__ == "__main__":
    main()