def hangman():
    allScores = []
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

    goOn = True
    while goOn:
        maxScore = 0
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
                if guessed_L in guessed_letters:
                    print("YOU ALREADY GUESSED THIS LETTER")
            if guessed_L in answer:
                maxScore +=1
                
                for i in range(len(answer)):
                    if answer[i] == guessed_L:
                        hint[i] = guessed_L
                        guessed_letters.add(guessed_L)
            else:
                incorrect_guesses += 1
                hangman_display(incorrect_guesses)
            if incorrect_guesses >= 6:
                hangman_display(incorrect_guesses)
                allScores.append(maxScore)
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
                allScores.append(maxScore)
                break
        while True:
            try:
                gameContinue = input("Do You Want To Play Again? Y/N  ").lower().strip()
                if gameContinue not in ["y", "n"]:
                    raise ValueError("Invalid choice. Please enter Y or N.")
                break
            except ValueError as e:
                print(e)
        if gameContinue == "y":
            continue
        else:
            goOn = False
    print(allScores)

    try:
        with open(r"C:\Users\ACER\Desktop\Vortex\Training Phase 1\Python Fundementals\SW-Training-Phase1-2025\S2SW\Hangman\hangmanLeaderBoard.txt", 'r') as file:
            allLeaderBoard = file.readlines()
    except FileNotFoundError:
        allLeaderBoard = []

    try:
        allLeaderBoard = [int(line.strip()) for line in allLeaderBoard if line.strip().isdigit()]
    except ValueError:
        print("Error reading leaderboard data. Some entries might be corrupted.")
        return

    allLeaderBoard.extend(allScores)
    allLeaderBoard = list(set(allLeaderBoard)) 
    allLeaderBoard.sort(reverse=True)

    with open(r"C:\Users\ACER\Desktop\Vortex\Training Phase 1\Python Fundementals\SW-Training-Phase1-2025\S2SW\Hangman\hangmanLeaderBoard.txt", 'w') as file:
        for score in allLeaderBoard:
            file.write(f"{str(score)}\n")

    print("Leaderboard Updated:", allLeaderBoard)



hangman()