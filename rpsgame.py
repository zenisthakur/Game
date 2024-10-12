import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("400x300")
        self.options = {"rock", "paper", "scissors"}
        self.score = {"wins": 0, "losses": 0, "ties": 0}
        self.label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Helvetica", 14))
        self.label.pack(pady=10)
        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play("rock"), width=10, bg="lightblue")
        self.rock_button.pack(side=tk.LEFT, padx=5)

        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play("paper"), width=10, bg="lightgreen")
        self.paper_button.pack(side=tk.LEFT, padx=5)

        self.scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play("scissors"), width=10, bg="lightcoral")
        self.scissors_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(list(self.options))
        result = self.determine_winner(user_choice, computer_choice)

        if result == "You win!":
            self.score["wins"] += 1
        elif result == "You lose!":
            self.score["losses"] += 1
        else: 
            self.score["ties"] += 1

        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}.\n{result}")
        self.score_label.config(text=self.get_score_text())

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return "You win!"
        else:
            return "You lose!"

    def get_score_text(self):
        return f"Wins: {self.score['wins']} | Losses: {self.score['losses']} | Ties: {self.score['ties']}"

root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
