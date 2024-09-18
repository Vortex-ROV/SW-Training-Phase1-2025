import os
import random

LEADERBOARD_FILE = "quiz_game_leaderboard.txt"

def load_leaderboard():
    leaderboard = {}
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                leaderboard[name] = int(score)
    return leaderboard

def save_leaderboard(leaderboard):
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

    with open(LEADERBOARD_FILE, "w") as file:
        for name, score in sorted_leaderboard.items():
            file.write(f"{name}:{score}\n")


def update_leaderboard(player_name, score, leaderboard):
    if player_name in leaderboard:
        leaderboard[player_name] += score
    else:
        leaderboard[player_name] = score
    save_leaderboard(leaderboard)
    

# Define questions as a list of tuples (question, answer)
leaderboard = load_leaderboard()
questions = [
    ("What is the capital of France? ", "Paris"),
    ("What is the largest planet in the solar system? ", "Jupiter"),
    ("What is the square root of 64? ", "8"),
    ("Who wrote 'Hamlet'? ", "Shakespeare"),
    ("What is the chemical symbol for water? ", "H2O")
]

# Ask a single question
def ask_question(question, correct_answer, user_input):
    return (user_input == correct_answer, 10 if user_input == correct_answer else 0)

# Ask all questions
def ask_all_questions(questions, get_user_input):
    return [ask_question(q, a, get_user_input(q)) for q, a in questions]

# Check if the player has lost
def check_loss(answers):
    return len([a for a, score in answers if not a]) >= 3

# Calculate total score
def calculate_score(answers):
    return sum([score for _, score in answers])

# Print results
def print_results(score, name):
    print(f"\n{name}, your final score is {score} points.")
    if score >= 30:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost!")

# Run the game
def run_quiz_game():
    name = get_user_input("What is your name? ")
    
    answers = ask_all_questions(questions, get_user_input)
    
    if check_loss(answers):
        print(f"\nSorry, {name}, you got 3 answers wrong. Game over.")
    else:
        score = calculate_score(answers)
        update_leaderboard(name, score, leaderboard)
        print_results(score, name)
    return game_end_options()
# Function to simulate user input (replace with input for real play)
def get_user_input(prompt):
    return input(prompt)


# Function to display game end options with input validation
def game_end_options():
    while True:
        print("1) Play again")
        print("2) Main menu")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                return True  # Play again
            elif option == 2:
                return False  # Go back to menu
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
