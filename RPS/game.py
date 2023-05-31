# import random

# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break

import random
import tkinter as tk
from tkinter import messagebox

def play_game():
    user_action = user_choice.get()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!"
    elif user_action == "rock":
        if computer_action == "scissors":
            result = "Rock smashes scissors! You win!"
        else:
            result = "Paper covers rock! You lose."
    elif user_action == "paper":
        if computer_action == "rock":
            result = "Paper covers rock! You win!"
        else:
            result = "Scissors cuts paper! You lose."
    elif user_action == "scissors":
        if computer_action == "paper":
            result = "Scissors cuts paper! You win!"
        else:
            result = "Rock smashes scissors! You lose."
    
    result_label.config(text=result)

def restart_game():
    user_choice.set("")
    result_label.config(text="")

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("300x250")
window.resizable(False, False)
window.configure(background="#F5F5F5")

user_choice = tk.StringVar()

title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Helvetica", 16, "bold"), bg="#F5F5F5")
title_label.pack(pady=10)

choice_label = tk.Label(window, text="Enter your choice:", font=("Helvetica", 12), bg="#F5F5F5")
choice_label.pack()

entry = tk.Entry(window, textvariable=user_choice, font=("Helvetica", 12), justify="center")
entry.insert(0, "rock, paper, scissors")
entry.pack()

play_button = tk.Button(window, text="Play", command=play_game, font=("Helvetica", 12), bg="#4CAF50", fg="white")
play_button.pack(pady=10)

restart_button = tk.Button(window, text="Restart", command=restart_game, font=("Helvetica", 12), bg="#F44336", fg="white")
restart_button.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 12, "bold"), bg="#F5F5F5")
result_label.pack(pady=20)

window.mainloop()





