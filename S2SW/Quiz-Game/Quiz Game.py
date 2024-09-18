def QuizGame():
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

