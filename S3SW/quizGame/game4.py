import json
import random

def quiz_game():
 LEADERBOARD_FILE = 'S3SW\quizGame\leaderboard.json'      ##### PATH LINK #####

 def load_questions(file_path):
    with open(file_path, 'r') as file:                         #open the JOSN file and read it
        questions = json.load(file)
    return questions

 def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as file:              # open the leaderboard and read it
            content = file.read().strip()  
            if not content:                                    # avoiding the error happens during the first time the game is run or an empty file
                return []                                      
            leaderboard = json.loads(content)                  
    except FileNotFoundError:                                  # avoiding the error happens if the file is missing
        leaderboard = []
    except json.JSONDecodeError as e:                          # will handle any problem with the (json content) by initializing an empty leaderboard.
        print(f"Error decoding JSON: {e}")
        leaderboard = []
    return leaderboard


 def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, 'w') as file:
        json.dump(leaderboard, file, indent=4)                  # Save the leaderboard in a formatted readable json file
 def update_leaderboard(player_name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({"name": player_name, "score": score})
    filtered_leaderboard = [entry for entry in leaderboard if entry.get("score") is not None and isinstance(entry["score"], int)]     # filter the invalid scores 
    filtered_leaderboard = sorted(filtered_leaderboard, key=lambda x: x["score"], reverse=True)    # sort the scores in descending order
    filtered_leaderboard = filtered_leaderboard[:10]
    save_leaderboard(filtered_leaderboard)



 def quiz_Random(questions):
    random.shuffle(questions)
    score = 0
    live = 3
    
    for question in questions:
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        
        answer = input("Your answer (A, B, C, D): ").strip().upper()
        
        while answer != question["correct"]:
            live -= 1
            if live <= 0:
                print("You have no lives left. Game over.")
                break
        
            print(f"Wrong! You have {live} live/s left. Try again.")
            answer = input("Your answer (A, B, C, D): ").strip().upper()
        
        if live <= 0:
            break
        
        if answer == question["correct"]:
            print("Correct!")
            score += 1
        
        print()
    
    retry =input("Do you need to Retry?(yes/no):").strip().lower()
    if retry== 'yes':
        score = 0
        questions = load_questions('S3SW\quizGame\questions.json')                   ##### PATH LINK #####
        quiz_Random(questions)
    else:
        print(f"Quiz finished! {player_name} Your score is {score} out of {len(questions)}.")
        return score

 def display_leaderboard():
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("No leaderboard data available.")
        return
    
    print("Leaderboard:")
    for entry in leaderboard:
        print(f"{entry['name']}: {entry['score']}")


 while True:
        player_name = input("Enter your name: ").strip()
        questions = load_questions('S3SW\quizGame\questions.json')                                   ##### PATH LINK #####
        score = quiz_Random(questions)
        update_leaderboard(player_name, score)
    
        while True:
            choice = input("Do you want to (1) play again (2) Exit or (3) See the leaderboard? Enter 1, 2, or 3: ").strip()
            if choice == '1':
                  questions = load_questions('S3SW\quizGame\questions.json')                                   ##### PATH LINK #####
                  score = quiz_Random(questions)
                  update_leaderboard(player_name, score)                                         # Exit this inner loop to restart the game
            elif choice == '2':
                print("Thank you for playing! Goodbye.")
                break                                              # Exit the program
            elif choice == '3':
                display_leaderboard()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")   # stay in the while loop
        break        
               