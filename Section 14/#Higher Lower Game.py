import random       
import os
from game_data import data
from art import logo,vs

def format_data(account):
    """Fotmat thr account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess,a_follower,b_follower):
    """Use if statement to check if user is correct and return if they got right"""
    if a_follower > b_follower:
        return guess == "a" #True ถ้า guess เป็น a    
    else:
        return guess == "b" #False ถ้า guess เป็น b    

print(logo)
score = 0

account_b = random.choice(data) #เพื่อไม่ให้เข้าไป loop ในเกม

game_should_continue = True
while game_should_continue:
    #Make account at B to A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")
    guess = input("Who has more followers? 'A' or 'B' : ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    os.system('cls||clear')
    if is_correct:
        score += 1
        print(f"You're right!, Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False


