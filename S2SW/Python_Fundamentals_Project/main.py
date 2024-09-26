from Quiz_Game import quiz_game
from Hangman import hangman
from Guess_Number import guess_number
from Tic_Tac_Toe import tic_tac_toe
from Word_Scramble import word_scramble


def play():
    print(f"Game Options:")
    print(f"Quiz Game: 1")
    print(f"Hangman: 2")
    print(f"Guessing Number: 3")
    print(f"Tic Tac Toe: 4")
    print(f"Word Scramble: 5")

    while True:
        try:
            num = int(input("Enter a number between 1 and 5: "))
            if num not in range(1, 6):
                raise ValueError("Invalid choice. Please enter number 1-5")
            break
        except ValueError:
            print("Invalid choice. Please enter number 1-5")
    print()
    match num:
        case 1:
            quiz_game.game_loop()
        case 2:
            hangman.game_loop()
        case 3:
            guess_number.game_loop()
        case 4:
            tic_tac_toe.game_loop()
        case 5:
            word_scramble.game_loop()
        case _:
            print("\nNumber not between 1 and 5")


if __name__ == "__main__":
    while True:
        play()
        while True:
            try:
                continueInput = input("Do you want to try another game? Y/N ").lower().strip()
                if continueInput not in ["y", "n"]:
                    print("Invalid choice. Please enter Y or N.")
                else:
                    break
            except ValueError as e:
                print(e)

        if continueInput == "n":
            break
