import os 
import random


def hang_man_game():
 HANGMAN_PICS = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

 #LIST OF WORDS  
 words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


 # FUNCTION TO GET WORD FROM WORDS RANDOMLY 
 def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

 #DISPLAY BOARD 
 def displayBoard(missedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_PICS[len(missedLetters)])

    print()
    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Display the secret word with spaces between the letters
    for letter in blanks:
        print(letter, end =' ')
    print()


 # FUNCTION TO ENSURE THATT THE LETTER IS (SINGLE , NOT GUESSED BEFORE , IN ALPHAPET )
 def getGuess(alreadyGuessed):

    while True:
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

 #TO ASK THE PLAYER IF HE WANTS TO PLAY AGAIN OR NOT 
 def playAgain():
    print('Would you like to play again? (y)es or (n)o')
    response = input().lower()
    
    if response.startswith('y'):
        return True
    elif response.startswith('n'):
        print("Thank you for playing! Hope to see you again soon! ")
        return False
    else:
        print("Please enter (y)es or (n)o.")
        return playAgain()


 # FUNCTION TO UPDATE THE LEADERBOARD AND SORT BY SCORE
 def updateLeaderboard(name, score):
    leaderboard = []

    # Read the existing leaderboard data
    if os.path.exists("S3SW\hangManGame\game3.txt"):
        with open("S3SW\hangManGame\game3.txt", 'r') as file:
            for line in file:
                if line.strip():  # TO SKIP ANY EMPTY LINE 
                    entry = line.strip().split(': ')
                    if len(entry) == 2:  # Ensure correct format
                        leaderboard.append((entry[0], int(entry[1])))  # ADD TO THE LIST OF LEADER BOARED A PAIR TUPLES CONSIST OF (NAME , SCORE)

    # Add the new score
    leaderboard.append((name, score))

    # Sort the leaderboard by score in ascending order
    leaderboard.sort(key=lambda x: x[1], reverse=True)       #LAMBDA FN HELPS TO SORT ACcORDING TO THE [1] INDEX OF THE TUPLE AND DESCENDING


    # Write the sorted leaderboard back to the file
    with open("S3SW\hangManGame\game3.txt", 'w') as file:   
        for entry in leaderboard:
            file.write(f'{entry[0]}: {entry[1]}\n')


        
        
 print('|_H_A_N_G_M_A_N_|')
 missedLetters = ''
 correctLetters = ''
 secretWord = getRandomWord(words)
 gameIsDone = False

 #  THE MAIN LOOP OF THE GAME 
 while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Let the player enter a letter 
    
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check to see if the player has won:
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You guessed it!')
            print('The secret word is "' + secretWord + '"! You win!')
            gameIsDone = True
            
            # Calculate the score
            score = 10 * len(correctLetters) - 5 * len(missedLetters)
            print(f'Your score is: {score}')
            name = input('Enter your name for the leaderboard: ')
            updateLeaderboard(name, score)
    else:
        missedLetters = missedLetters + guess

        # Check if the player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
             # Calculate the score
            score = 10 * len(correctLetters) - 5 * len(missedLetters)
            print(f'Your score is: {score}')
            name = input('Enter your name for the leaderboard: ')
            updateLeaderboard(name, score)
            
            
    # to ask the player to try again.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
        