import customtkinter as ctk
from tkinter import messagebox
import random

# ------------------ SETTINGS ------------------ #
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

MAX_ATTEMPTS = 5

# ------------------ WINDOW ------------------ #
app = ctk.CTk()
app.title("🎯 Secret Number Guessing Game")
app.geometry("550x500")
app.resizable(False, False)

# ------------------ GAME VARIABLES ------------------ #
secret_number = random.randint(1000, 9999)
attempts_left = MAX_ATTEMPTS

# ------------------ FUNCTIONS ------------------ #
def update_hearts():
    hearts = "❤️ " * attempts_left
    empty = "🖤 " * (MAX_ATTEMPTS - attempts_left)
    attempts_label.configure(text=f"Attempts: {hearts}{empty}")

def reset_game():
    global secret_number, attempts_left

    secret_number = random.randint(1000, 9999)
    attempts_left = MAX_ATTEMPTS

    guess_entry.delete(0, "end")
    hint_label.configure(text="💡 Hint will appear here")
    update_hearts()

    guess_button.configure(state="normal")

def game_over():
    guess_button.configure(state="disabled")

def check_guess(event=None):
    global attempts_left

    guess = guess_entry.get().strip()

    if not guess.isdigit() or len(guess) != 4:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid 4-digit number."
        )
        return

    guess = int(guess)

    if guess == secret_number:
        hint_label.configure(text="🎉 Correct Guess!")
        game_over()

        messagebox.showinfo(
            "Congratulations!",
            f"You guessed the secret number!\n\nNumber = {secret_number}"
        )

        reset_game()
        return

    attempts_left -= 1
    update_hearts()

    if guess < secret_number:
        hint_label.configure(text="📉 Too Low!")
    else:
        hint_label.configure(text="📈 Too High!")

    if attempts_left == 0:
        game_over()

        messagebox.showerror(
            "Game Over",
            f"You lost!\n\nSecret Number = {secret_number}"
        )

        reset_game()

    guess_entry.delete(0, "end")

# ------------------ UI ------------------ #

title = ctk.CTkLabel(
    app,
    text="🎯 Secret Number Guessing Game",
    font=("Arial", 26, "bold")
)
title.pack(pady=(20, 10))

subtitle = ctk.CTkLabel(
    app,
    text="Guess the secret 4-digit number",
    font=("Arial", 16)
)
subtitle.pack()

guess_entry = ctk.CTkEntry(
    app,
    width=250,
    height=45,
    font=("Arial", 18),
    placeholder_text="Enter your guess..."
)
guess_entry.pack(pady=25)

guess_entry.bind("<Return>", check_guess)

guess_button = ctk.CTkButton(
    app,
    text="🎯 Guess",
    width=200,
    height=45,
    font=("Arial", 16),
    command=check_guess
)
guess_button.pack()

attempts_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 20)
)
attempts_label.pack(pady=25)

hint_label = ctk.CTkLabel(
    app,
    text="💡 Hint will appear here",
    font=("Arial", 18)
)
hint_label.pack()

new_game_button = ctk.CTkButton(
    app,
    text="🔄 New Game",
    width=200,
    height=45,
    font=("Arial", 16),
    command=reset_game
)
new_game_button.pack(pady=35)

update_hearts()

app.mainloop()