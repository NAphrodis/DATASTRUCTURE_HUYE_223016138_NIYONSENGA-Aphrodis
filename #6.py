#6.Create a 2D array that represents a 3x3 tic-tac-toe board, and check if there's a winner.
board = [['a', 'o', 'a'],
         ['a', 'o', 'a'],
         ['o', 'a', 'o']
        ]
# check the winner from the board

def check_winner(board):
# check the winner for rows and column
  for i in range(3):
    if board[i][0]==board[i][1]==board[i][2] and board[i][0] !='_':
      return f"winner is  {board[i][0]}"
    if board[0][i]==board[1][i]==board[2][i] and board[0][i] !='_':
     return f"winner is {board[0][i]}"
    #check for diagonal
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] !='_':
      return f"winner is {board[0][0]}"
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2] !='_':
      return f"winner is {board[0][2]}"
    
  return f"no winner"
print(check_winner(board))
