
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

def check_winner(board, player):
    """Check if the player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Check if board is full (draw condition)"""
    return all(cell != " " for row in board for cell in row)

def get_player_move(board, player):
    """Get valid move from player"""
    while True:
        try:
            position = int(input(f"Player {player}, enter position (1-9): "))
            if position < 1 or position > 9:
                print("Enter number between 1-9!")
                continue
            row, col = (position - 1) // 3, (position - 1) % 3
            if board[row][col] != " ":
                print("Position already taken!")
                continue
            return row, col
        except ValueError:
            print("Enter a valid number!")
def play_game():
    """Main game loop"""
