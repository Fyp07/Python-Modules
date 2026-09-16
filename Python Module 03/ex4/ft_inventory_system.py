
import sys

# def add_item

# sword:1 stick:6


def create_inverntory() -> dict:
    inventory: dict = {}

    for i in sys.argv[1:]:
        try:
            args: list[str] = i.split(":")

            if len(args) != 2:
                print("Error — Invalid format: expecting [key]:[value]")
                continue

            key, value = args
            if key.capitalize() in inventory:
                print(f"Item '{key}' already exists in "
                      "the inventory — discarding")
                continue
            else:
                inventory[key.capitalize()] = int(value)
        except ValueError as e:
            print(f"Quantity error for 'key': {e}")

    return inventory


def print_inventory(inventory: dict) -> None:
    print("=" * 35)
    print(f"{'Inventory':^35}")
    print("=" * 35)

    print(f"{'Item':<10}{'Quantity':>24}")
    print("-" * 35)

    for key, value in inventory.items():
        print(f"{key:<10} {value:>22}x")
        print("-" * 35)


def main() -> None:
    inventory: dict = create_inverntory()
    if not inventory:
        print("No arguments provided by the user. usage: [key]:[value]")
        return

    print_inventory(inventory)

    item_list: list = list(inventory.keys())
    items_quantity: int = sum(inventory.values())

    print(f"Item list: {item_list}")
    print(f"Total quantity of the {len(item_list)} item(s): {items_quantity}")
    for key, value in inventory.items():
        percentage = (value / items_quantity) * 100
        print(f"Item {key} represents {percentage:.1f}%")

    most_abundant: str = item_list[0]
    least_abundant: str = item_list[0]

    for item in item_list:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        elif inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} "
          f"with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} "
          f"with quantity {inventory[least_abundant]}")

    inventory.update({"Magic Item": 4})
    print_inventory(inventory)


if __name__ == "__main__":
    main()
