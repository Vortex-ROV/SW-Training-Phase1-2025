"""
- The game has two modes: Player vs. Player and Player vs. Computer.
- The game continues until one player wins.
- The winner takes 5 points.

Game flow:
- The player chooses the game mode.
- The players enter their names (player2 = "AI Agent" in Player vs. Computer mode).
- The game starts.
- The players take turns to play (AI Agent uses the minimax algorithm).
- The game continues until one player wins, or it is a draw.
- The user decides to play with the same player or to exit the game.
- The winner takes 5 points.
- The leaderboard is displayed.
- The user decides to play again or to exit the game.

Leaderboard:
- The leaderboard is saved in a file named "leaderboard.txt".
- The leaderboard is updated after each game.
- The leaderboard is displayed in descending order.
- The leaderboard is displayed in the following format:
    1. Player Name: Score
    2. Player Name: Score
    3. Player Name: Score
    4. Player Name: Score
    5. Player Name: Score
- If the player-name exists in the leaderboard, the score is updated (by adding the new score to the old one).
- If the player-name does not exist in the leaderboard, the player-name and score are added to the leaderboard.

Functions:
- game_mode(): Choose the game mode.
- print_board(board): Print the game board.
- player_game(board, player, game='X'): Player's turn.
- computer_game(board): AI Agent's turn.
- check_winner(board, player): Check if a player wins.
- player_vs_player(): Player vs. Player mode.
- player_vs_computer(): Player vs. Computer mode.
- update_leaderboard(scores): Update the leaderboard.
- display_leaderboard(): Display the leaderboard.
- play_again(): Ask the user if they want to play again.
- game_loop(): Main game loop.
"""
from minimax import Minimax


def game_mode():
    while True:
        try:
            mode = input("Choose the game mode:\n1. Player vs. Player\n2. Player vs. Computer\n").strip()
            if mode not in ["1", "2"]:
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            break
        except ValueError as e:
            print(e)
    return mode


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | "
          f"{board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n")


def player_game(board, player, game='X'):
    while True:
        try:
            move = int(input(f"{player}, Enter Your Move (1-9): ").strip())
            if board[move - 1] == " ":
                board[move - 1] = game
                break
            else:
                print("Invalid Move. Try Again.")
        except (ValueError, IndexError):
            print("Invalid Move. Try Again.")


def computer_game(board):
    minimax = Minimax(max_depth=5)
    best_move = minimax.get_best_move(board, 'O')
    board[best_move] = 'O'


def check_winner(board, player):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combination in win_combinations:
        if all([board[i] == player for i in combination]):
            return True
    return False


def player_vs_player():
    while True:
        player1 = input("Enter Player 1 Name: ").strip()
        if player1 == "AI Agent":
            print("This name is dedicated for the computer. Please, enter another name.")
        else:
            break
    while True:
        player2 = input("Enter Player 2 Name: ").strip()
        if player2 == "AI Agent":
            print("This name is dedicated for the computer. Please, enter another name.")
        elif player2 == player1:
            print("This name is already taken. Please, enter another name.")
        else:
            break
    players = [player1, player2]
    scores = {player1: 0, player2: 0}

    game = 'X'
    reverse_game_dict = {'X': 'O', 'O': 'X'}
    while True:
        board = [" " for _ in range(9)]
        print_board(board)
        temp = game

        while True:
            game_ended = False
            for player in players:
                player_game(board, player, game)
                print_board(board)
                game = reverse_game_dict[game]

                if check_winner(board, "X"):
                    print(f"{player1} Wins!")
                    scores[player1] += 5
                elif check_winner(board, "O"):
                    print(f"{player2} Wins!")
                    scores[player2] += 5
                elif " " not in board:
                    print("It's a Draw!")
                else:
                    continue
                game_ended = True
                break
            if game_ended:
                break

        if play_again() == "n":
            break

        game = reverse_game_dict[temp]
        players.reverse()

    update_leaderboard(scores)


def player_vs_computer():
    player1 = input("Enter Player 1 Name: ").strip()
    player2 = "AI Agent"
    players = [player1, player2]
    scores = {player1: 0, player2: 0}

    while True:
        board = [" " for _ in range(9)]
        print_board(board)

        while True:
            game_ended = False
            for player in players:
                if player == player1:
                    player_game(board, player)
                else:
                    computer_game(board)
                print_board(board)

                if check_winner(board, "X"):
                    print(f"{player1} Wins!")
                    scores[player1] += 5
                elif check_winner(board, "O"):
                    print(f"{player2} Wins!")
                    scores[player2] += 5
                elif " " not in board:
                    print("It's a Draw!")
                else:
                    continue
                game_ended = True
                break

            if game_ended:
                break

        if play_again() == "n":
            break

        players.reverse()

    update_leaderboard(scores)


def update_leaderboard(scores):
    file_path = r"leaderboard.txt"
    try:
        with open(file_path, 'r') as file:
            linesList = file.readlines()
    except FileNotFoundError:
        linesList = []

    linesList = [line.strip().split(':') for line in linesList]
    linesList = {line[0]: int(line[1]) for line in linesList}

    for player, score in scores.items():
        if player in linesList:
            linesList[player] += score
        else:
            linesList[player] = score

    linesList = {k: v for k, v in sorted(linesList.items(), key=lambda item: item[1], reverse=True)}

    with open(file_path, 'w') as file:
        for player, score in linesList.items():
            file.write(f"{player}: {score}\n")


def display_leaderboard():
    file_path = r"leaderboard.txt"
    try:
        with open(file_path, 'r') as file:
            linesList = file.readlines()
    except FileNotFoundError:
        linesList = []

    print("Leaderboard:")
    for line in linesList[:5]:
        print(line.strip())


def play_again():
    while True:
        try:
            replay = input("Do You Want To Play Again? Y/N  ").lower().strip()
            if replay not in ["y", "n"]:
                raise ValueError("Invalid choice. Please enter Y or N.")
            break
        except ValueError as e:
            print(e)
    return replay


def game_loop():
    while True:
        mode = game_mode()
        if mode == "1":
            player_vs_player()
        else:
            player_vs_computer()
        display_leaderboard()
        input("Press Enter To Continue...")
        if play_again() == "n":
            break


if __name__ == "__main__":
    game_loop()
