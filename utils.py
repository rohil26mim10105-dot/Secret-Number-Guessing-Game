def calculate_difference(guess, secret_number):
    return abs(secret_number - guess)


def calculate_attempts_left(current_attempt, max_attempts):
    return max_attempts - current_attempt