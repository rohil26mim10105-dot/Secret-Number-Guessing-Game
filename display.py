import random


def show_welcome():
    print("=" * 40)
    print("SECRET NUMBER GUESSING GAME".center(40))
    print("=" * 40)
    print("Guess the 4-digit secret number.")
    print("You have 5 attempts.")
    print()


def show_attempt(attempt, max_attempts):
    print(f"\nAttempt: {attempt}/{max_attempts}")


def show_attempts_left(attempts_left):
    print(f"Attempts left: {attempts_left}")


def show_success():
    print("\nCongratulations! You guessed the number correctly.")


def show_game_over(secret_number):
    print("\nGame Over!")
    print("You used all your attempts.")
    print(f"The secret number was: {secret_number}")


def main():
    secret_number = random.randint(1000, 9999)
    max_attempts = 5

    show_welcome()

    for attempt in range(1, max_attempts + 1):
        show_attempt(attempt, max_attempts)

        while True:
            guess = input("Enter your guess: ")

            if guess.isdigit() and len(guess) == 4:
                guess = int(guess)
                break
            else:
                print("Please enter a valid 4-digit number.")

        if guess == secret_number:
            show_success()
            break

        elif guess < secret_number:
            print("Too low!")

        else:
            print("Too high!")

        attempts_left = max_attempts - attempt
        if attempts_left > 0:
            show_attempts_left(attempts_left)

    else:
        show_game_over(secret_number)


if __name__ == "__main__":
    main()