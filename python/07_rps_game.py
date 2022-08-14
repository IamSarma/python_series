# This is a Rock, Paper, Scissors game.
import random
import sys

# These variables keep track of wins, losses and ties.
wins, losses, ties = 0, 0, 0

# The main game loop
while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    # The player input loop
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_choice = input()
        if player_choice == "q":
            sys.exit()
        if player_choice == "r" or player_choice == "p" or player_choice == "s":
            break
        print("Type one of r, p, s or q.")

    # Display what the player chose.
    if player_choice == "r":
        print("ROCK versus...")
    elif player_choice == "p":
        print("PAPER versus...")
    elif player_choice == "s":
        print("SCISSORS versus...")

    # Display what the computer chose.
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_choice = "r"
        print("ROCK")
    elif random_number == 2:
        computer_choice = "p"
        print("PAPER")
    elif random_number == 3:
        computer_choice = "s"
        print("SCISSORS")

    # Display and record the win/loss/tie.
    if player_choice == computer_choice:
        print("It is a tie!")
        ties += 1
    elif player_choice == "r":
        if computer_choice == "p":
            print("You lose!")
            losses += 1
        elif computer_choice == "s":
            print("You won!")
            wins += 1
    elif player_choice == "p":
        if computer_choice == "s":
            print("You lose!")
            losses += 1
        elif computer_choice == "r":
            print("You won!")
            wins += 1
    elif player_choice == "s":
        if computer_choice == "r":
            print("You lose!")
            losses += 1
        elif computer_choice == "p":
            print("You won!")
            wins += 1
