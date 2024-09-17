scores = []

try:
    with open("Questions.txt", 'r') as file:
        linesList = file.readlines()
except FileNotFoundError:
    linesList = []

linesList = [line.strip() for line in linesList]

gameOn = True
while gameOn:

    questionAmount = 0
    j = 0

    while j < len(linesList):
        questionAmount += 1
        j += 6

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
            questionAmount -= 1
            points += 1
            print(f"Score: {points}")
            if (questionAmount == 0):
                print("Congratulation You Finished!")
            else:
                print(f"Amount Of Questions Remaining: {questionAmount}\n")
        else:
            lives -= 1
            questionAmount -= 1
            if (questionAmount == 0 and lives == 0):
                print(f"Score: {points}")
                print("Out of Lives :(")
            elif (questionAmount == 0):
                print("Congratulation You Finished!")
                print(f"Score: {points}")
            else:
                print(f"Incorrect Answer! Remaining Lives: {lives}")
                print(f"Score: {points}\n")
        i += 6  # Move to the next question block

    scores.append(points)

    while True:
        try:
            print("\n")
            gameContinue = input("Do You Want To Play Again? Y/N  ").lower().strip()
            print("\n")
            if gameContinue not in ["y", "n"]:
                raise ValueError("Invalid choice. Please enter Y or N.")
            break
    
        except ValueError as e:
            print(e)

    if gameContinue == "y":
        continue
    else:
        print(scores)
        gameOn = False



try:
    with open("QuizGame Leaderboard.txt", 'r') as file:
        allLeaderBoard = file.readlines()
except FileNotFoundError:
    allLeaderBoard = []

allLeaderBoard = [line.strip() for line in allLeaderBoard if line.strip().isdigit()]
allLeaderBoard = [int(score) for score in allLeaderBoard]

allLeaderBoard.extend(scores)
allLeaderBoard = list(set(allLeaderBoard))

allLeaderBoard.sort(reverse=True)

with open("QuizGame Leaderboard.txt", 'w') as file:
    for score in allLeaderBoard:
        file.write(f"{str(score)}\n")


