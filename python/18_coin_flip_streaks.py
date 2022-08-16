# Fun experiment to calculate chances of streak for 6 consecutive heads or tails
# out of list with randomly generated values of 100 heads or tails
# for 10000 sample iterations
import random

number_of_streaks = 0

for num in range(10000):
    # Create a list of 100 heads or tails
    main_list = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            main_list.append("H")
        else:
            main_list.append("T")

    # Check if there is a streak of 6 heads or tails in a row
    heads_counter, tails_counter = 0, 0
    for value in main_list:
        if value == "H":
            heads_counter += 1
            tails_counter = 0
        elif value == "T":
            tails_counter += 1
            heads_counter = 0

        if heads_counter == 6 or tails_counter == 6:
            heads_counter, tails_counter = 0, 0
            number_of_streaks += 1
            break

print(f"Chance of streak: {(number_of_streaks / 100):.2f}%")
