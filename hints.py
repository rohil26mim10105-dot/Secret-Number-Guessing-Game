def get_hint(guess, secret_number):

    if guess < secret_number:

        difference = secret_number - guess

        if difference <= 100:
            return "Extremely close! Enter a bit higher."

        elif difference <= 500:
            return "Enter a higher number."

        else:
            return "Enter a much higher number."

    elif guess > secret_number:

        difference = guess - secret_number

        if difference <= 100:
            return "Extremely close! Enter a bit lower."

        elif difference <= 500:
            return "Enter a lower number."

        else:
            return "Enter a much lower number."

    return "Correct!"