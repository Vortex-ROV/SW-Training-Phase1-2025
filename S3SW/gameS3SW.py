from gussingGame.game1 import gussing_game
from scrambleGame.game2 import scrambleGame
from hangManGame.game3 import hang_man_game

def play():  #play method that show the games menu
  while True: 
    print("what do you want to play:\n1)tic-tac-toe\n2)quizGame\n3)wordScramble\n4)gussingGame\n5)hangManGame\n6)Exit")  
    y = int(input("please enter 1,2,3,4,5,6"))
    match y:
        case 1:
            print("tic-tac-toe") #mkan el print htb2a elmethod
        case 2:
            print("quizGame") #mkan el print htb2a elmethod    
        case 3:
            scrambleGame()      
        case 4:
            gussing_game()
        case 5: 
            hang_man_game()
        case 6 :
            break    
def leaderBord():
    
    print("choose one :\n1)tic-tac-toe\n2)quizGame\n3)wordScramble\n4)gussingGame\n5)hangManGame\n6)Exit")  
    i = int(input("please enter 1,2,3,4,5,6"))
    match i:
        case 1:
            print("tic-tac-toe") #mkan el print htb2a elmethod
        case 2:
            print("quizGame") #mkan el print htb2a elmethod    
        case 3:
            file=open("S3SW\scrambleGame\game2.txt")
            print(file.read())
            file.close
        case 4:
             file=open("S3SW\gussingGame\game1.txt")
             print(file.read())
             file.close
        case 5: 
             file=open("S3SW\hangManGame\game3.txt")
             print(file.read())
             file.close
                 
while True:
 print("welcome to our game the playgroud\n1) play\n2) leaderBord\n3) Exit")
 x = int(input("please enter 1,2,3"))
 match x:
  case 1 :
      play()  
  case 2 :
      leaderBord()
  case 3 :
      break    
