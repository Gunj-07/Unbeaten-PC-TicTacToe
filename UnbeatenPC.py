import tkinter as tk
from tkinter import messagebox
from playsound import playsound

root = tk.Tk()
root.title("Tic Tac Toe: Unbeatable PC")

buttons = [[None for _ in range(3)] for _ in range(3)]
board = [["" for _ in range(3)] for _ in range(3)]

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_full():
    for row in board:
        if "" in row:
            return False
    return True

def on_click(row, col):
    if board[row][col] == "" and not check_winner():
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled",fg="black")
        winner = check_winner()
        if winner == "O":
            playsound("C:/Users/parma/Desktop/PY project/sound/funny-laughing-sound-effect.mp3")
            messagebox.showinfo("Game Over"," PC wins! YOU ARE A LOOSER !!!")
            disable_all_buttons()
            return
        elif winner == "X":
            playsound("C:/Users/parma/Desktop/PY project/sound/oh-no-the-car-exploded.mp3")
            messagebox.showinfo("Game Over"," YOU WIN ! PC IS A LOOSER !!!")
            disable_all_buttons()
            return
        elif is_full():
            playsound("C:/Users/parma/Desktop/PY project/sound/beated-by-a-computer-by-tromosm.mp3")
            messagebox.showinfo("Game Over", "It's a draw!")
            return
        root.after(100, pc_move)  # Let PC play after 0.1 sec delay

def pc_move():
    best_score = -float('inf')
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                score = minimax(board, 0, False)
                board[r][c] = ""
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    if best_move:
        r, c = best_move
        board[r][c] = "O"
        buttons[r][c].config(text="O", state="disabled",fg="black")
        winner = check_winner()
        if winner == "O":
            playsound("C:/Users/parma/Desktop/PY project/sound/funny-laughing-sound-effect.mp3")
            messagebox.showinfo("Game Over"," PC wins! YOU ARE A LOOSER !!!")
            disable_all_buttons()
            return
        elif winner == "X":
            playsound("C:/Users/parma/Desktop/PY project/sound/oh-no-the-car-exploded.mp3")
            messagebox.showinfo("Game Over"," YOU WIN ! PC IS A LOOSER !!!")
            disable_all_buttons()
            return
        elif is_full():
            playsound("C:/Users/parma/Desktop/PY project/sound/beated-by-a-computer-by-tromosm.mp3")
            messagebox.showinfo("Game Over", "It's a draw!")
            return
def minimax(board_state, depth, is_maximizing):
    winner = check_winner()
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == "":
                    board_state[r][c] = "O"
                    score = minimax(board_state, depth + 1, False)
                    board_state[r][c] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == "":
                    board_state[r][c] = "X"
                    score = minimax(board_state, depth + 1, True)
                    board_state[r][c] = ""
                    best_score = min(score, best_score)
        return best_score

def disable_all_buttons():
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(state="disabled")

def new_game():
    for r in range(3):
        for c in range(3):
            board[r][c] = ""
            buttons[r][c].config(text="", state="normal")

for r in range(3):
    for c in range(3):
        b = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                      command=lambda r=r, c=c: on_click(r, c))
        b.grid(row=r, column=c)
        buttons[r][c] = b

reset_button = tk.Button(root, text="RESTART",bg="black",fg="white", font=("Arial", 20), command=new_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
