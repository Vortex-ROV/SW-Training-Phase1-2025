def leaderboardHangman():
    try:
        with open(r"C:\Users\ACER\Desktop\Vortex\Training Phase 1\Python Fundementals\SW-Training-Phase1-2025\S2SW\Hangman\hangmanLeaderBoard.txt", 'r') as file:
            linesList = file.readlines()
    except FileNotFoundError:
        print("Questions file not found.")
        return
    print("\nTOP SCORES WITH MOST ANSWERED QUESTIONS!")
    print("="*42)
    for lines in linesList:
        print(lines)
        print("="*42)


def leaderboardQuizGame():
    try:
        with open(r"C:\Users\ACER\Desktop\Vortex\Training Phase 1\Python Fundementals\SW-Training-Phase1-2025\S2SW\Main-Game\QuizGame Leaderboard.txt", 'r') as file:
            linesList = file.readlines()
    except FileNotFoundError:
        print("Questions file not found.")
        return
    print("\nTOP SCORES WITH MOST ANSWERED QUESTIONS!")
    print("="*42)
    for lines in linesList:
        print(lines)
        print("="*42)


def leadebroardGuessingNumber():
    try:
        with open(r"C:\Users\ACER\Desktop\Vortex\Training Phase 1\Python Fundementals\SW-Training-Phase1-2025\S2SW\Main-Game\guessNumberLeaderboard.txt", 'r') as file:
            linesList = file.readlines()
    except FileNotFoundError:
        print("Questions file not found.")
        return
    print("\n TOP SCORES WITH LEAST AMOUNT OF TRIES!")
    print("="*42)
    for lines in linesList:
        print(lines)
        print("="*42)

def leaderboardTicTacToe():
    pass

def leaderboardWordScramble():
    pass


def leaderboard():
    print(f"\nGame Options:")
    print(f"LeaderBoard Hangman: 1")
    print(f"LeaderBoard Quiz-Game: 2")
    print(f"LeaderBoard Guessing-Number: 3")
    print(f"LeaderBoard Tic-Tac-Toe: 4")
    print(f"LeaderBoard Word-Scramble: 5")

    while True:
        try:
            num = int(input("\nEnter a number between 1 and 5: "))
            if num not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid choice. Please enter number 1-5")
            break
        except ValueError as e:
            print("Invalid choice. Please enter number 1-5")

    match num:
        case 1:
            leaderboardHangman()
            breakpoint
        case 2:
            leaderboardQuizGame()
            breakpoint
        case 3:
            leadebroardGuessingNumber()
            breakpoint
        case 4:
            pass
        case 5:
            pass
        case _:
            print("\nNumber not between 1 and 5")


leaderboardRepeats = True
while leaderboardRepeats:

    leaderboard()

    while True:
        try:
            repeatsInput = input("Do you want to see another leaderboard? Y/N  ").lower().strip()
            if repeatsInput not in ["y", "n"]:
                raise ValueError("Invalid choice. Please enter Y or N.")
            break
        except ValueError as e:
            print(e)

    if repeatsInput == "n":
        leaderboardRepeats = False

leaderboard()