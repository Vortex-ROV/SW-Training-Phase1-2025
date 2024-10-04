"""
Board shape:
|~~~|~~~|~~~|
|~~~|~~~|~~~|
|~~~|~~~|~~~|
|~~~|~~~|~~~|~~~|
|~~~|~~~|~~~|~~~|
|~~~|~~~|~~~|~~~|~~~|
Scrambled List: [A, B, C, D, E, F]

Rules:
|~~~|~~~|~~~|
|~~~|~~~|~~~|
|~~~|~~~|~~~|
|~~~|~~~|~~~|~~~|
|~~~|~~~|~~~|~~~|
|~~~|~~~|~~~|~~~|~~~|
- This is the part where the words should be put.
- Every '|~~~|' is a cell
- Every cell contains a letter of a horizontal word.
- Now, the game should have three words of length 3, three words of length 4, and one word of length 5.

Scrambled List: [A, B, C, D, E, F]
- This is the part where a scrambled set of letters will appear for the player.
- The player should write a word with only the letters in the scrambled set.
- If the player writes a valid word, then his score will increase by 10.
- If the player writes an invalid word, then his score will decrease by 5.
- If the player writes a bonus word (Not written in the board), then his score will increase by 5.

Possible games:
1- Game #1:
- valid_words = ["CAT", "BAT", "TAB", "TACK", "BACK", "STACK"]
- scrambled_list = ["C", "A", "T", "B", "K", "S"]

2- Game #2:
- valid_words = ["PIN", "NIP", "TIN", "PINT", "TINT", "PRINT"]
- scrambled_list = ["P", "I", "N", "T", "R", "T"]

3- Game #3:
- valid_words = ["DOG", "GOD", "DOT", "GOOD", "TOOD", "GODOT"]
- scrambled_list = ["D", "O", "G", "T", "O", "O"]

4- Game #4:
- valid_words = ["CAR", "ARC", "BAR", "BARK", "RACK", "CRACK"]
- scrambled_list = ["C", "A", "R", "B", "K", "C"]

5- Game #5:
- valid_words = ["HEN", "TEN", "NET", "TENT", "HEAT", "NEATH"]
- scrambled_list = ["H", "E", "N", "T", "A", "T"]

Game flow:
- The player writes his name.
- The player chooses a game from the possible games.
- The player writes a word.
- If the word is valid, then the player's score will increase by 10, and the word is written in the board.
- If the word is invalid, then the player's score will decrease by 5.
- If the word is a bonus word, then the player's score will increase by 5.
- If the word is already written in the board, then the player should try another word.
- When the game ends, the leaderboard will appear with the top 5 players, then the player decides to play again or not.
- If the player decides to play again, then the game flow will start again.

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
- print_board(words, scrambled_list): prints the board with the words and the scrambled list.
- not_full(words): returns True if there is a cell in the board that is not filled with a word.
- update_leaderboard(player, score): updates the leaderboard with the player's name and score.
- display_leaderboard(): displays the leaderboard.
- start_game(): starts the game.
- play_again(): returns True if the player wants to play again.
- game_loop(): the main game loop.
"""
import os
import json
from collections import Counter
from english_words import get_english_words_set

with open('game_data.json', 'r') as game_data:
    GAMES_DICT = json.load(game_data)

ENGLISH_WORDS = set(word.upper() for word in get_english_words_set(["web2"]))


def print_board(words, scrambled_list):
    print('\n'.join(f"|{'|'.join(f'~{cell}~' for cell in word)}|" for word in words))
    print(f'Scrambled List: {scrambled_list}\n')


def is_bonus(word, scrambled_list):
    if word not in ENGLISH_WORDS:
        return False
    word_counter = Counter(word)
    scrambled_counter = Counter(scrambled_list)
    return all(word_counter[letter] <= scrambled_counter[letter] for letter in word_counter)


def load_leaderboard():
    if not os.path.exists("leaderboard.json"):
        return {}
    try:
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f)


def update_leaderboard(player, score):
    leaderboard = load_leaderboard()
    leaderboard[player] = leaderboard.get(player, 0) + score
    save_leaderboard(leaderboard)


def display_leaderboard():
    leaderboard = load_leaderboard()

    if not leaderboard:
        print("Leaderboard is empty.")
        return

    print("Leaderboard:")
    for i, (player, score) in enumerate(sorted(leaderboard.items(), key=lambda x: x[1], reverse=True), 1):
        print(f"{i}. {player}: {score}")
    print()


def start_game():
    player = input("Enter Player Name: ").strip()
    game = input("Choose a game from the possible games (1-5): ").strip().replace(" ", "")
    print()

    valid_words, scrambled_list = GAMES_DICT[game]
    words: list = ["~" * len(word) for word in valid_words]
    score = 0
    used_words = set()

    while "~" in "".join(words):
        print_board(words, scrambled_list)
        word = input("Enter a Word: ").strip().upper()

        if word in used_words:
            print("Word Already Used. Try Another Word.")
        elif word in valid_words:
            print("Valid Word!")
            score += 10
            words[valid_words.index(word)] = word
            used_words.add(word)
        elif is_bonus(word, scrambled_list):
            print("Bonus Word!")
            score += 5
            used_words.add(word)
        else:
            print("Invalid Word!")
            score = max(0, score - 5)

        print(f'Your score is: {score}\n')

    update_leaderboard(player, score)
    return score


def game_loop():
    while True:
        start_game()
        display_leaderboard()
        if input("Play Again? (y/n): ").strip().lower() != 'y':
            break


if __name__ == "__main__":
    game_loop()
