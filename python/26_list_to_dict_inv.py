# Function to add input list items to existing dictionary
def addToInventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


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


inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventory = addToInventory(inventory, dragon_loot)
displayInventory(inventory)
