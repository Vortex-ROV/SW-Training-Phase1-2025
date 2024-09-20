import random

# Function to print the game board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("--" * 5)

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    if [player] * 3 in win_conditions:
        return True
    return False

# Function to check if there is a tie
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function for the player's move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Invalid move! Spot already taken.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")

# Minimax algorithm for AI move
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if check_tie(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

# Function for AI move using Minimax
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "O"
                score = minimax(board, 0, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    if best_move:
        board[best_move[0]][best_move[1]] = "O"
        print(f"AI chooses spot {best_move[0] * 3 + best_move[1] + 1}")

# Main function to play the game
def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        print("Welcome to Tic-Tac-Toe!")
        mode = input("Choose mode: '1' for Human vs Human, '2' for Human vs AI (random), '3' for Human vs AI (smart): ")
        current_player = "X"
        game_over = False

        while not game_over:
            print_board(board)
            
            if mode == "1" or current_player == "X":
                player_move(board, current_player)
            elif mode == "2" and current_player == "O":
                # Random AI
                available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
                move = random.choice(available_moves)
                board[move[0]][move[1]] = "O"
                print(f"AI (random) chooses spot {move[0] * 3 + move[1] + 1}")
            elif mode == "3" and current_player == "O":
                # Smart AI using Minimax
                ai_move(board)
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        
        if input("Play again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    play_game()