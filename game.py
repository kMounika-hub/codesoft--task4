import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create the buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: play_game('Paper'))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: play_game('Scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Create the label to display the result
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors")
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
