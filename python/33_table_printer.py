# Function to display input in a well-organized tabluar format
def printTable(table_data):
    max_len = 0
    # Finding maximum lenth to perform right justify
    for data in table_data:
        for item in data:
            if len(item) > max_len:
                max_len = len(item)

    # Displaying data in tabular format
    item_index = 0
    while item_index <= len(table_data):
        for data in table_data:
            print(data[item_index].rjust(max_len), end="")
        print()
        item_index += 1


table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "mosse", "goose"]
]

printTable(table_data)
