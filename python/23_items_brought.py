# Example of using nested dictionary 👌
guests = {
    "Alice": {
        "apples": 5,
        "pretzels": 12
    },
    "Bob": {
        "ham sandwiches": 3,
        "apples": 2
    },
    "Carol": {
        "cups": 3,
        "apple pies": 1
    }
}


def total_items_brought(guests, item):
    items_brought = 0

    for value in guests.values():
        items_brought += value.get(item, 0)

    return items_brought


print("Number of things being brought:")
print(" - Apples            " + str(total_items_brought(guests, "apples")))
print(" - Pretzles          " + str(total_items_brought(guests, "pretzels")))
print(" - Ham Sandwiches    " + str(total_items_brought(guests, "ham sandwiches")))
print(" - Cups              " + str(total_items_brought(guests, "cups")))
print(" - Apple Pies        " + str(total_items_brought(guests, "apple pies")))
