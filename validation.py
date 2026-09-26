guess = int(input("Enter your secret_number:"))

def get_valid_guess():
    while True:
        user_input = input("Enter a 4 digit number: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1000 or guess > 9999:
            print("Please enter a 4 digit number.")
            continue

        return guess








