import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

MAX_ATTEMPTS=5

class GuessGame:
    def __init__(self):
        self.root=ctk.CTk()
        self.root.title("Secret Number Guessing Game")
        self.root.geometry("500x430")
        self.root.resizable(False,False)
        self.new_game()

        ctk.CTkLabel(self.root,text="🎯 Secret Number Guessing Game",
                     font=("Arial",24,"bold")).pack(pady=20)
        ctk.CTkLabel(self.root,text="Guess the 4-digit secret number",
                     font=("Arial",15)).pack()

        self.entry=ctk.CTkEntry(self.root,width=220,height=40,
                                placeholder_text="Enter 4-digit number")
        self.entry.pack(pady=20)
        self.entry.bind("<Return>",self.check_guess)

        self.btn=ctk.CTkButton(self.root,text="Guess",
                               command=self.check_guess)
        self.btn.pack()

        self.attempt_label=ctk.CTkLabel(self.root,font=("Arial",16))
        self.attempt_label.pack(pady=20)

        self.hint=ctk.CTkLabel(self.root,text="Hint will appear here",
                               font=("Arial",16))
        self.hint.pack()

        ctk.CTkButton(self.root,text="New Game",
                      command=self.reset).pack(pady=30)
        self.update_status()

    def new_game(self):
        self.secret=random.randint(1000,9999)
        self.left=MAX_ATTEMPTS

    def hearts(self):
        return "❤️"*self.left+"🖤"*(MAX_ATTEMPTS-self.left)

    def update_status(self):
        self.attempt_label.configure(
            text=f"Attempts: {self.hearts()} ({self.left}/{MAX_ATTEMPTS})")

    def reset(self):
        self.new_game()
        self.entry.delete(0,"end")
        self.hint.configure(text="Hint will appear here")
        self.btn.configure(state="normal")
        self.update_status()

    def check_guess(self,event=None):
        text=self.entry.get().strip()
        if not(text.isdigit() and len(text)==4):
            messagebox.showerror("Invalid","Enter a valid 4-digit number.")
            return
        guess=int(text)
        self.entry.delete(0,"end")

        if guess==self.secret:
            self.hint.configure(text="🎉 Correct!")
            self.btn.configure(state="disabled")
            messagebox.showinfo("Congratulations",
                                f"You guessed {self.secret} correctly!")
            self.reset()
            return

        self.left-=1

        if guess<self.secret:
            self.hint.configure(text="📉 Too Low")
        else:
            self.hint.configure(text="📈 Too High")

        self.update_status()

        if self.left==0:
            self.btn.configure(state="disabled")
            messagebox.showerror("Game Over",
                                 f"The secret number was {self.secret}")
            self.reset()

    def run(self):
        self.root.mainloop()

if __name__=="__main__":
    GuessGame().run()
