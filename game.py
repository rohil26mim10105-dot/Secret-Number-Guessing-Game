from config import SECRET_NUMBER, MAX_ATTEMPTS
from validation import get_valid_guess
from hints import get_hint
from display import (
    show_attempt,
    show_attempts_left,
    show_success,
    show_game_over
)


def play_game():
    attempts = 0

    while attempts < MAX_ATTEMPTS:

        attempts += 1

        show_attempt(attempts, MAX_ATTEMPTS)

        guess = get_valid_guess()

        if guess == SECRET_NUMBER:
            show_success()
            return True

        hint = get_hint(guess, SECRET_NUMBER)
        print(hint)

        attempts_left = MAX_ATTEMPTS - attempts
        show_attempts_left(attempts_left)

    show_game_over(SECRET_NUMBER)
    return False