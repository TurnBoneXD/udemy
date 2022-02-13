from art import logo
import random
import os

def random_number():
    number = []
    for num in range(100):
        number.append(num+1)
    return int(random.choice(number))

def hint():
    if user_guess > CORRECT_NUMBER:
        return "Too high."
    elif user_guess < CORRECT_NUMBER:
        return "Too low."
    elif user_guess == CORRECT_NUMBER:
        return f"You got it! The anwser was {CORRECT_NUMBER}."


def select_difficulty(mode):
    global user_guess
    is_game_end = False
    while not is_game_end:  
        for round in range(mode,0,-1):
            print(f"You have {round} attempts remaining to guess a number.")
            user_guess = int(input("Make a guess : "))
            if user_guess == CORRECT_NUMBER:
                print(hint())
                print("-----------------------------------------------------------------")
                break
            elif round == 1:
                print(f"You lose! The anwser was {CORRECT_NUMBER}.")
                print("-----------------------------------------------------------------")
            else:
                print(hint())
                print("Guess again")
                print("-----------------------------------------------------------------")
        is_game_end = True

def play_game(): 
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm think of a number beetween 1 too 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == "easy":
        mode = 10 #round guess
        select_difficulty(mode)
    elif difficulty == "hard":
        mode = 5 #round guess
        select_difficulty(mode)

while input("Do you want to play again? Type 'Y' or 'N' : ").upper() == "Y":
    os.system('cls||clear')
    CORRECT_NUMBER = random_number()
    play_game()
