import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break
        elif abs(guess - number_to_guess) <= 5:
            print("🔥 Very close!")
        elif guess < number_to_guess:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

if __name__ == "__main__":
    number_guessing_game()
