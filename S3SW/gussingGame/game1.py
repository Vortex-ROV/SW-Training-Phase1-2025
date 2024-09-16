import random


def gussing_game():
    def addpoint(score):
        return score + 1

    tries = 1
    wins = 0
    randomNumber = random.randint(1, 10)

    name = input("Hello, What's your name?: ")
    print("okay! " + name + " I am guessing a number between 1 and 10: (guess the number three times to win!)")
    while tries < 4:
        guess = int(input())
        if randomNumber > guess:
            print("Your guess is too low")
            tries = tries + 1
            continue
        elif randomNumber < guess:
            print("Your guess is too high")
            tries = tries + 1
            continue
        elif randomNumber == guess:
            print("You guessed the number in", tries, "tries!")
            wins = addpoint(wins)
            print("Your score is currently:", wins)
            randomNumber = random.randint(1, 10)
            tries = 1
            if wins == 3:
                print("You have won the game!")
                break
            else:
             print("Let's go again! Keep guessing, win 3 rounds to win the game.")
             continue
    else:
      print("game over! you could not guess the number in 3 tries")


    while True:
     again = input("do you want to play again? (yes/no): ")
     if again == "yes":
      tries = 1
      wins = 0
      randomNumber = random.randint(1, 10)

      print("okay! " + name + " I am guessing a number between 1 and 10: (guess the number three times to win!)")
      while tries < 4:
        guess = int(input())
        if randomNumber > guess:
            print("Your guess is too low")
            tries = tries + 1
            continue
        elif randomNumber < guess:
            print("Your guess is too high")
            tries = tries + 1
            continue
        elif randomNumber == guess:
            print("You guessed the number in", tries, "tries!")
            wins = addpoint(wins)
            print("Your score is currently:", wins)
            randomNumber = random.randint(1, 10)
            tries = 1
            if wins == 3:
                print("You have won the game!")
                break
            else:
                print("Let's go again! Keep guessing, win 3 rounds to win the game.")
                continue
      else:
          print("game over! you could not guess the number in 3 tries")
     elif again=="no":
        print("Thanks for playing")
        break  