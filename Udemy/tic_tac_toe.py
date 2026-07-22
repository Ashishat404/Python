
# Tic Tac Toe Game in Python
# Steps:
# 1. Create a 3x3 board
# 2. Display the board
# 3. Get player input
# 4. Check for valid moves
# 5. Check for winning conditions
# 6. Alternate between players (X and O)
# 7. Check for draw
# 8. Repeat until game ends


def greet():
#    """Greet the players and explain the rules"""
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'.")

def print_board(board):
    """Display the current board state"""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")
