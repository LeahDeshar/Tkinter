import tkinter as tk
from tkinter import ttk, messagebox
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
    if player == "Draw":
        message = "It's a draw!"
    else:
        message = f"Player {player} wins!"
    messagebox.showinfo("Game Over!", message)
    reset_game()


def reset_game():
    global game, current_player
    game = [['', '', ''] for _ in range(3)]
    current_player = "X"
    for row in buttons:
        for button in row:
            button.configure(text=" ", style="primary.TButton",state="normal")


def make_move(row, col):
    global current_player

    if game[row][col] == '':
        game[row][col] = current_player
        buttons[row][col].configure(text=current_player,style="info.TButton")
        check_winner()
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        feedback_label.config(text=f"Current turn: {current_player}")


root = tk.Tk()
root.title("Tic-Tae-Toe")
root.resizable(False,False)
style = Style(theme="flatly")

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = ttk.Button(root, text=" ", width=20, style="primary.TButton", command=lambda i=i, j=j: make_move(i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

feedback_label = ttk.Label(root, text="Current turn: X", style="info.TLabel")
feedback_label.grid(row=3, column=0, columnspan=3, pady=10)

game = [['', '', ''] for _ in range(3)]
current_player = "X"

root.mainloop()
