import random
from db.db import *

def guess_game(range_limit):
    target_number = random.randint(0, range_limit)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Try greater >")
            elif guess > target_number:
                print("Try smaller <")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                save_game_data(target_number, attempts, range_limit)
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run
try:
    use_case = input("\"Play\" to play and \"View\" to view: ")
    if use_case == "View":
        get_all_game_data()
    elif use_case == "Play":
        try:
            range_limit = int(input("Enter your range: "))
            if range_limit < 0:
                print("Range must be a non-negative integer.")
            else:
                guess_game(range_limit)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        raise ValueError("Wrong_Input")  # Raising a ValueError for invalid input
except ValueError as e:
    print(f"Error: {e}")

