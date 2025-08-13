"""
RULES:
Snake drinks water → Snake wins
Gun shoots snake → Gun wins
Water damages gun → Water wins """

import random
import os

# File to store high score
HIGHSCORE_FILE = "highscore.txt"


def load_highscore():
    """Load the high score from file or return 0 if file doesn't exist."""
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0


def save_highscore(score):
    """Save the high score to file."""
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))


def snake_water_gun():
    choices = ['snake', 'water', 'gun']
    emojis = {'snake': '🐍', 'water': '💧', 'gun': '🔫'}

    high_score = load_highscore()

    while True:
        print("\n=== Snake 🐍  Water 💧  Gun 🔫 ===")
        print("Rules: Snake drinks Water, Gun shoots Snake, Water damages Gun")
        print(f"🎯 Current High Score: {high_score}")
        print("\nMenu:")
        print("1. Play Game")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == '2':
            print("👋 Thanks for playing! Goodbye.")
            break
        elif choice != '1':
            print("❌ Invalid option! Try again.")
            continue

        # Game loop until player quits mid-game
        user_score = 0
        comp_score = 0

        while True:
            user_choice = input("\nEnter your choice (snake/water/gun) or 'q' to quit: ").lower()

            if user_choice == 'q':
                print(f"Final Score → You: {user_score} | Computer: {comp_score}")
                if user_score > high_score:
                    print("🎉 New High Score! 🏆")
                    save_highscore(user_score)
                break

            if user_choice not in choices:
                print("❌ Invalid choice! Please choose snake, water, or gun.")
                continue

            comp_choice = random.choice(choices)
            print(f"Computer chose: {comp_choice} {emojis[comp_choice]}")

            # Game logic
            if user_choice == comp_choice:
                print("😐 It's a Tie!")
            elif (user_choice == 'snake' and comp_choice == 'water') or \
                    (user_choice == 'water' and comp_choice == 'gun') or \
                    (user_choice == 'gun' and comp_choice == 'snake'):
                print("✅ You win this round!")
                user_score += 1
            else:
                print("💻 Computer wins this round!")
                comp_score += 1

            print(f"Score → You: {user_score} | Computer: {comp_score}")



if __name__ == "__main__":
    snake_water_gun()

