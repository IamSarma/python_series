# Example of how to use ljust(), rjust() and center()
def printPicnicItems(picnic_items, left_width, right_width):
    print("PICNIC ITEMS".center(left_width + right_width, "-"))
    for item, quantity in picnic_items.items():
        print(item.ljust(left_width, ".") + str(quantity).rjust(right_width))


picnic_items = {
    "sandwiches": 4,
    "apples": 12,
    "cups": 4,
    "cookies": 8000
}
printPicnicItems(picnic_items, 12, 5)
printPicnicItems(picnic_items, 20, 6)
