import random

goOn = True
scores = []

while goOn:
    randomNumber = random.randint(1, 5)
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
            gameContinue = input("Do You Want To Play Again? Y/N  ").lower().strip()
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

# Will fix the file path when merging code.
file_path = r"leaderboard.txt"

try:
    with open(file_path, 'r') as file:
        linesList = file.readlines()
except FileNotFoundError:
    linesList = []

linesList = [line.strip() for line in linesList if line.strip().isdigit()]
linesList = [int(score) for score in linesList]

linesList.extend(scores)
linesList = list(set(linesList))

linesList.sort()

with open(file_path, 'w') as file:
    for score in linesList:
        file.write(f"{str(score)}\n")
