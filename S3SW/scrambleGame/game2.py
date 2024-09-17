import random

def scrambleGame():
    word_list = ['python', 'computer', 'programming', 'scramble', 'algorithm', 'data', 'science','vortex','labtop']
    file2=open("S3SW\scrambleGame\game2.txt","a")
    def scramble_word(word):
       scrambled = list(word)
       random.shuffle(scrambled)
       return ''.join(scrambled)
    gamesWon=0
    word = random.choice(word_list)    
    scrambled_word = scramble_word(word)
    
    name =input("enter your name")
    print(f"okay {name} Welcome to the Word Scramble Game try to guess in 3 try's ")
    print(f"Scrambled word: {scrambled_word}") 
    x=1
    while x<4:
        guess = input("Guess the word: ").lower()
        
        if guess == word:
            print("Congratulations! You guessed the word correctly.")
            gamesWon+=1
            break
        else:
            print(f"Wrong guess! You have {3-x} attempts left.")
            x+=1
    else:
        print(f"Sorry, the correct word was: {word}")

    while True:
     tryAgain = input("do you want to play again? (yes/no): ")
     if tryAgain == "yes":
         
          word = random.choice(word_list)    
          scrambled_word = scramble_word(word)
    
          print(f"okay {name} Welcome to the Word Scramble Game try to guess in 3 try's ")
          print(f"Scrambled word: {scrambled_word}")
          j=1
          while j<4:
            guess = input("Guess the word: ").lower()
        
            if guess == word:
               print("Congratulations! You guessed the word correctly.")
               gamesWon+=1
               break
            else:
              print(f"Wrong guess! You have {3-x} attempts left.")
              j+=1    
          else:
           print(f"Sorry, the correct word was: {word}")
     elif tryAgain=="no":
         file2.write(name+": "+str(gamesWon)+"\n")
         file2.close
         break      
     
