def guessNumber():
    import random
    
    goOn = True
    scores = []

    while goOn:
        randomNumber = random.randint(1, 10)
        count = 1
        print("Try to guess the number!\n")

        while True:
            try:
                userInput = int(input(f"Try {count}: "))
                count += 1

                if userInput > randomNumber:
                    print("Try Guessing Lower!\n")
                elif userInput < randomNumber:
                    print("Try Guessing Higher!\n")
                else:
                    print(f"Congrats! Your Score Is : {count - 1} \n")
                    scores.append(count - 1)
                    break
            except ValueError:
                print("This Is Not A Number")

        while True:
            try:
                gameContinue = input("Do You Want To Play Again? Y/N  ").lower().strip()
                if gameContinue not in ["y", "n"]:
                    raise ValueError("Invalid choice. Please enter Y or N.")
                break
            except ValueError as e:
                print(e)

        if gameContinue == "y":
            continue
        else:
            print(scores)
            goOn = False


    try:
        with open("guessNumberLeaderboard.txt", 'r') as file:
            linesList = file.readlines()
    except FileNotFoundError:
        linesList = []

    linesList = [line.strip() for line in linesList if line.strip().isdigit()]
    linesList = [int(score) for score in linesList]

    linesList.extend(scores)
    linesList = list(set(linesList))

    linesList.sort()

    with open("guessNumberLeaderboard.txt", 'w') as file:
        for score in linesList:
            file.write(f"{str(score)}\n")


def quizGame():
    scores = []
    try:
        with open(r"C:\Users\ACER\Desktop\Vortex\Training Phase 1\Python Fundementals\SW-Training-Phase1-2025\S2SW\Questions.txt", 'r') as file:
            linesList = file.readlines()
    except FileNotFoundError:
        print("Questions file not found.")
        return

    if len(linesList) % 6 != 0:
        print("Questions file is not properly formatted. Each question must have exactly 6 lines.")
        return

    linesList = [line.strip() for line in linesList]

    gameOn = True
    while gameOn:

        questionAmount = len(linesList) // 6 
        lives = 3
        i = 0
        points = 0

        while i < len(linesList) and lives > 0:
            print(linesList[i])
            print(f" {linesList[i+1]}")
            print(f" {linesList[i+2]}")
            print(f" {linesList[i+3]}")
            print(f" {linesList[i+4]}")

            while True:
                try:
                    userAnswer = input("Please Enter A/B/C/D: ").strip().lower()
                    if userAnswer not in ["a", "b", "c", "d"]:
                        raise ValueError("Invalid choice. Please enter A/B/C/D")
                    break
                except ValueError as e:
                    print(e)

            if userAnswer == linesList[i+5].strip().lower():
                print("Correct!")
                points += 1
                print(f"Score: {points}")
            else:
                lives -= 1
                print(f"Incorrect Answer! Remaining Lives: {lives}")
                print(f"Score: {points}")

            questionAmount -= 1
            i += 6  # Move to the next question block

        scores.append(points)

        while True:
            try:
                gameContinue = input("Do You Want To Play Again? Y/N  ").lower().strip()
                if gameContinue not in ["y", "n"]:
                    raise ValueError("Invalid choice. Please enter Y or N.")
                break
            except ValueError as e:
                print(e)

        if gameContinue == "n":
            gameOn = False

    try:
        with open("QuizGame Leaderboard.txt", 'r') as file:
            allLeaderBoard = file.readlines()
    except FileNotFoundError:
        allLeaderBoard = []

    try:
        allLeaderBoard = [int(line.strip()) for line in allLeaderBoard if line.strip().isdigit()]
    except ValueError:
        print("Error reading leaderboard data. Some entries might be corrupted.")
        return

    allLeaderBoard.extend(scores)
    allLeaderBoard = list(set(allLeaderBoard)) 
    allLeaderBoard.sort(reverse=True)

    with open("QuizGame Leaderboard.txt", 'w') as file:
        for score in allLeaderBoard:
            file.write(f"{str(score)}\n")

    print("Leaderboard Updated:", allLeaderBoard)


def hangman():

    import time
    import random

    name = input("WHAT IS YOUR NAME :")
    Words = ("vortex", "pineapple", "keyboard", "computer", "carpet",
            "house", "table", "chair", "office", "plane", "machine", "fridge")
    hangman_view = {0: ("  ",
                        "  ",
                        "  "),
                    1: (" o ",
                        "  ",
                        "  "),
                    2: (" o ",
                        " | ",
                        "  "),
                    3: (" o ",
                        "/| ",
                        "  "),
                    4: (" o ",
                        "/|\\ ",
                        "  "),
                    5: (" o ",
                        "/|\\",
                        "/ "),
                    6: (" o ",
                        "/|\\",
                        "/ \\")}


    def hangman_display(wrong_guess):
        print("---------------")
        for line in hangman_view[wrong_guess]:
            print(line)
        print("---------------")


    def spaces(hints):
        print(" ".join(hints))


    def answer(answer):
        pass


    answer = random.choice(Words)
    guessed_letters = set()
    hint = ["_"] * len(answer)
    incorrect_guesses = 0
    while True:
        hangman_display(incorrect_guesses)
        spaces(hint)
        guessed_L = input("Enter a letter").lower()
        while len(guessed_L) != 1 or not guessed_L.isalpha():
            guessed_L = input("Please select a singular alphabetical letter")
            if guessed_L in guessed_letters():
                print("YOU ALREADY GUESSED THIS LETTER")
        if guessed_L in answer:
            for i in range(len(answer)):
                if answer[i] == guessed_L:
                    hint[i] = guessed_L
                    guessed_letters.add(guessed_L)
        else:
            incorrect_guesses += 1
            hangman_display(incorrect_guesses)
        if incorrect_guesses >= 6:
            hangman_display(incorrect_guesses)
            print(f"YOU LOST {name} ")
            print()
            print(f"THE ANSWER WAS {answer}")
            print()
            break
        if "_" not in hint:
            print()
            spaces(hint)
            print()
            print(f"YOU WON {name} ")
            break


def runMatch():
    num = int(input("Enter a number between 1 and 3: "))
    match num:
        case 1:
            guessNumber()
            breakpoint
        case 2:
            quizGame()
            breakpoint
        case 3:
            hangman()
            breakpoint
        case _:
            print("Number not between 1 and 3")
        
        
gameRepeats = True
while gameRepeats:
    
    runMatch()

    while True:
        try:
            continueInput = input("Do you want to try another game? Y/N  ").lower().strip()
            if continueInput not in ["y", "n"]:
                raise ValueError("Invalid choice. Please enter Y or N.")
            break
        except ValueError as e:
            print(e)

    if continueInput == "n":
        gameRepeats = False

