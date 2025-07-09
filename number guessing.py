import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    target = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Get the user's guess as an integer
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            # Handle non-integer inputs
            print("That's not a valid number. Please try again.")
            continue

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
