from gussingGame.game1 import gussing_game

def play():  #play method that show the gmes menu
  while True: 
    print("what do you want to play:\n1)tic-tac-toe\n2)quizGame\n3)wordScramble\n4)gussingGame\n5)hangManGame\n6)Exit")  
    y = int(input("please enter 1,2,3,4,5,6"))
    match y:
        case 1:
            print("tic-tac-toe") #mkan el print htb2a elmethod
        case 2:
            print("quizGame") #mkan el print htb2a elmethod    
        case 3:
            print("wordScramble") #mkan el print htb2a elmethod
        case 4:
            gussing_game()
        case 5: 
            print("hangManGame") #mkan el print htb2a elmethod
        case 6 :
            break    
             
while True:
 print("welcome to our game the playgroud\n1) play\n2) leaderBord\n3) Exit")
 x = int(input("please enter 1,2,3"))
 match x:
  case 1 :
      play()   #mkan el print htb2a elmethod
  case 2 :
      print("leaderBord")    #mkan el print htb2a elmethod
  case 3 :
      break    
