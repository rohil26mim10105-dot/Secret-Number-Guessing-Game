# 🎯 Secret Number Guessing Game

A beginner-friendly Python project where the player has to guess a randomly generated **4-digit secret number** within a limited number of attempts.

This project demonstrates the use of Python fundamentals including functions, loops, conditional statements, modules, input validation, and random number generation.

---

## 📌 Table of Contents

- About
- Features
- Technologies Used
- Project Structure
- How It Works
- Installation
- Usage
- Sample Output
- Python Concepts Used
- Future Improvements
- Learning Outcomes
- Author
- License

---

# 📖 About

The Secret Number Guessing Game is a command-line application written in Python.

The game randomly generates a 4-digit number. The player has **5 attempts** to guess the correct number.

After every incorrect guess, the game provides a hint:

- 📈 Too High
- 📉 Too Low

The game continues until the player either guesses correctly or runs out of attempts.

---

# ✨ Features

- 🎯 Random 4-digit secret number
- 🔢 Input validation
- 📈 Too High hint
- 📉 Too Low hint
- ❤️ Limited attempts
- 🏆 Winning message
- ❌ Game Over screen
- 🧩 Modular code structure
- 📚 Beginner friendly
- 🚀 Easy to customize

---

# 🛠 Technologies Used

- Python 3
- Random Module
- Functions
- Loops
- Conditional Statements
- Input Validation

---

# 📂 Project Structure

```
Secret-Number-Guessing-Game
│
├── guess_number.py
├── config.py
├── display.py
├── game.py
├── hints.py
├── utils.py
├── validation.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ How It Works

1. The program generates a random 4-digit secret number.
2. The player enters a guess.
3. The program checks the input.
4. If the guess is incorrect:
   - Too High
   - Too Low
5. Attempts decrease after every wrong guess.
6. If the player guesses correctly:
   - Congratulations message.
7. If all attempts are used:
   - Game Over message.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/rohil26mim10105-dot/Secret-Number-Guessing-Game.git
```

Go to the project folder

```bash
cd Secret-Number-Guessing-Game
```

Run the game

```bash
python guess_number.py
```

---

# 🎮 Sample Output

```
========================================
SECRET NUMBER GUESSING GAME
========================================

Guess the 4-digit secret number.

Attempt 1/5

Enter your guess: 4321

Too High!

Attempts Left: 4
```

---

# 📚 Python Concepts Used

- Variables
- Data Types
- User Input
- Functions
- Loops
- If-Else Statements
- Modules
- Random Library
- Error Handling
- Input Validation
- Code Reusability
- Program Flow

---

# 🎯 Learning Outcomes

This project helped in understanding:

- Function-based programming
- Modular programming
- Clean code organization
- Git and GitHub workflow
- README documentation
- Python project structure

---

# 🚀 Future Improvements

- GUI Version using Tkinter
- Difficulty Levels
- Multiplayer Mode
- Timer
- High Score System
- Sound Effects
- Statistics Dashboard
- Save Progress

---

# 👨‍💻 Author

**Rohil Khan**

Integrated M.Tech (CSE with AI)

VIT Bhopal University

GitHub:
https://github.com/rohil26mim10105-dot

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.bel = ctk.CTkLabel(
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