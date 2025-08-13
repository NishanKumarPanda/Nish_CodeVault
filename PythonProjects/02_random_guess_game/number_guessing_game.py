import random


def number_guessing_game():
    """
    A simple number guessing game.

    Rules:
    1. Program generates a random number between 1 and 100.
    2. User guesses until they get it correct.
    3. Hints are provided: 'Lower number please' or 'Higher number please'.
    4. The program displays the number of guesses taken.
    """
    print("🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Generate random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1  # Count each attempt

            if guess > target_number:
                print("📉 Lower number please.")
            elif guess < target_number:
                print("📈 Higher number please.")
            else:
                print(f"✅ You are correct!! The number was {target_number}.")
                print(f"🏆 You guessed it in {attempts} attempts.")
                break  # Exit loop once guessed correctly

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    number_guessing_game()

