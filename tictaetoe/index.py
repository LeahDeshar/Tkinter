import tkinter as tk
from tkinter import ttk, messagebox
import random
from ttkbootstrap import Style

def check_winner():
    winning_condition = (game[0], game[1], game[2],
                         [game[i][0] for i in range(3)],
                         [game[i][1] for i in range(3)],
                         [game[i][2] for i in range(3)],
                         [game[i][i] for i in range(3)],
                         [game[i][2 - i] for i in range(3)])
    for combination in winning_condition:
        if combination[0] == combination[1] == combination[2] != '':
            announce_winner(combination[0])
    if all(game[i][j] != '' for i in range(3) for j in range(3)):
        announce_winner("Draw")

def announce_winner(player):
    global human_score, computer_score
    if player == "Draw":
        message = "It's a draw!"
    else:
        message = f"Player {player} wins!"
        if player == "X":
            human_score += 1
        else:
            computer_score += 1
    messagebox.showinfo("Game Over!", message)
    update_score()
    reset_game()

def reset_game():
    global game, current_player
    game = [['', '', ''] for _ in range(3)]
    current_player = "X"
    for row in buttons:
        for button in row:
            button.configure(text=" ", style="primary.TButton", state="normal")
    feedback_label.config(text=f"Current turn: {current_player}")

def make_move(row, col):
    global current_player, human_turn
    if human_turn and game[row][col] == '':
        game[row][col] = current_player
        buttons[row][col].configure(text=current_player, style="info.TButton")
        check_winner()
        if not check_game_over():
            current_player = "O"
            feedback_label.config(text=f"Current turn: {current_player}")
            human_turn = False
            root.after(1000, computer_move)

def computer_move():
    global current_player, human_turn
    empty_cells = [(i, j) for i in range(3) for j in range(3) if game[i][j] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        game[row][col] = current_player
        buttons[row][col].configure(text=current_player, style="success.TButton")
        check_winner()
        if not check_game_over():
            current_player = "X"
            feedback_label.config(text=f"Current turn: {current_player}")
            human_turn = True

def check_game_over():
    if any(game[i][j] == '' for i in range(3) for j in range(3)):
        return False
    announce_winner("Draw")
    return True

def update_score():
    score_label.config(text=f"Human: {human_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Tic-Tae-Toe")
root.geometry("500x500+400+150")
root.resizable(False, False)
style = Style(theme="flatly")

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = ttk.Button(root, text=" ", width=20,style="primary.TButton", command=lambda i=i, j=j: make_move(i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        
        btn.grid(row=i, column=j, padx=5, pady=5, ipadx=5, ipady=40)
        row.append(btn)
    buttons.append(row)

feedback_label = ttk.Label(root, text="Current turn: X", style="info.TLabel",font=(13))
feedback_label.grid(row=3, column=0, columnspan=3, pady=10)

score_label = ttk.Label(root, text="Human: 0 | Computer: 0", style="info.TLabel",font=(10))
score_label.grid(row=4, column=0, columnspan=3, pady=10)

game = [['', '', ''] for _ in range(3)]
current_player = "X"
human_turn = True
human_score = 0
computer_score = 0

root.mainloop()
