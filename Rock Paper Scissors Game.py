import tkinter as tk
from tkinter import ttk
import random

def play():
    user_choice = user_var.get()
    computer_choice = random.choice(choices)

    result_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_var.set("You win!")
        user_score_var.set(user_score_var.get() + 1)
    else:
        result_var.set("Computer wins!")
        computer_score_var.set(computer_score_var.get() + 1)

def reset_scores():
    user_score_var.set(0)
    computer_score_var.set(0)

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]

user_var = tk.StringVar()
user_var.set("Rock")

user_frame = tk.Frame(root)
user_frame.pack(pady=10)

user_label = tk.Label(user_frame, text="Choose:", font=("Arial", 14))
user_label.pack(side=tk.LEFT)

user_menu = ttk.Combobox(user_frame, textvariable=user_var, values=choices, state="readonly", font=("Arial", 14))
user_menu.pack(side=tk.LEFT)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play, font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
play_button.pack()

result_var = tk.StringVar()
result_var.set("")

result_message = tk.Label(root, textvariable=result_var, font=("Arial", 16))
result_message.pack(pady=10)

scores_frame = tk.Frame(root)
scores_frame.pack(pady=10)

user_score_var = tk.IntVar()
user_score_var.set(0)

computer_score_var = tk.IntVar()
computer_score_var.set(0)

user_score_label = tk.Label(scores_frame, text="Your Score:", font=("Arial", 14))
user_score_label.pack(side=tk.LEFT)

user_score_display = tk.Label(scores_frame, textvariable=user_score_var, font=("Arial", 14))
user_score_display.pack(side=tk.LEFT, padx=10)

computer_score_label = tk.Label(scores_frame, text="Computer Score:", font=("Arial", 14))
computer_score_label.pack(side=tk.LEFT)

computer_score_display = tk.Label(scores_frame, textvariable=computer_score_var, font=("Arial", 14))
computer_score_display.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(root, text="Reset Scores", command=reset_scores, font=("Arial", 14), bg="#F44336", fg="white", padx=10, pady=5)
reset_button.pack(pady=10)

root.mainloop()
