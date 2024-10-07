#Multi-Dimensional Arrays:
# 6.Create a 2D array that represents a 3x3 tic-tac-toe board, and check if there's a winner.

board = [
    ['a', 'O', 'O'],
    ['O', 'O', 'a'],
    ['O', 'a', 'a']
]

# Check rows for a winner
winner = None
for row in board:
    if row[0] == row[1] == row[2] and row[0] != ' ':
        winner = row[0]

# Check columns for a winner
    elif winner is None:
     for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            winner = board[0][col]

# Check diagonals for a winner
    else: 
     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        winner = board[0][0]
     else:board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' '
winner = board[0][2]

# Print the result
if winner:
    print(f"The winner is {winner}")
else:
    print("No winner yet")