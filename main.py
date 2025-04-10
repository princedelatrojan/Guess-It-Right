# Word Guessing Game
import random
from art import logo

# Generate a random number between 1 and 100
guessed_number = random.randint(1, 100)

# Welcome message
print(logo)
print("🎉 Welcome to the Number Guessing Game! 🎯")
print("I'm thinking of a number between 1 and 100.")


# Choose game difficulty
def choose_difficulty():
    while True:
        mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if mode == "easy":
            return 10
        elif mode == "hard":
            return 5
        else:
            print("⚠️ Invalid input. Please type 'easy' or 'hard'.")


# Main game function
def game():
    attempts = choose_difficulty()
    # Uncomment below for testing
    # print(f"(Debug) The number is: {guessed_number}")

    while attempts > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("🚫 Please enter a valid number.")
            continue

        if guess == guessed_number:
            print(f"🎉 You got it! The number was {guessed_number}.")
            return
        elif guess > guessed_number:
            print("📈 Too high.")
        else:
            print("📉 Too low.")

        attempts -= 1
        if attempts > 0:
            print(f"🔁 You have {attempts} attempts remaining.\n")
        else:
            print(f"💀 You've run out of guesses. The number was {guessed_number}. Better luck next time!")


# Start the game
game()
