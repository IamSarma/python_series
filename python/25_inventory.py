# Function to display inventory items list and total items count
def displayInventory(input):
    total_items = 0
    print("Inventory:")

    try:
        for item, count in input.items():
            total_items += count
            print(f"{count} {item}")
    except:
        print("Item count should be a valid number")

    print(f"Total number of items: {total_items}")


inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

displayInventory(inventory)
