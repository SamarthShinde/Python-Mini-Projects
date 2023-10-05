import tkinter as tk

def on_click(row, col):
    if board[row][col] == ' ':
        global current_player
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner():
            label.config(text=f"Player {current_player} wins!")
            disable_buttons()
        elif is_board_full():
            label.config(text="It's a draw!")
            disable_buttons()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False
def is_board_full():
    return all(cell != ' ' for row in board for cell in row)

def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)

# Initialize board and player
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Create GUI window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the board
buttons = [[tk.Button(root, text=' ', font=('normal', 20), width=5, height=2, command=lambda i=i, j=j: on_click(i, j)) for j in range(3)] for i in range(3)]

# Place buttons in the window
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

# Create label for game status
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 14))
label.grid(row=3, column=0, columnspan=3)

# Run the GUI
root.mainloop()
