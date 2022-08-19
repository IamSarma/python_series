# Function to display input in a well-organized tabluar format
def printTable(table_data):
    max_len = 0
    # Finding maximum lenth to perform right justify
    for data in table_data:
        for item in data:
            if len(item) > max_len:
                max_len = len(item)


table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "mosse", "goose"]
]

printTable(table_data)
