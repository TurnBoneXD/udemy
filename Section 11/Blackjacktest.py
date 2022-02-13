from art import logo
import random
import os

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(cards)

def calculate(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    if sum(cards) == 21:
        return 0
    return sum(cards)

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "Bust!"
    elif user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Blackjack! You win"
    elif computer_score == 0:
        return "Opponent have Blackjcak!, you lose"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "Bust!"

def play_game():   
    
    print(logo) 
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate(user_card)
        computer_score = calculate(computer_card)
        print(f"Your cards : {user_card}, currency score : {user_score}")
        print(f"Computer first's cards : {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_selection = input("Type 'Deal' to get another card, type 'Stand' to pass : ").lower()
            print("-----------------------------------------------------------------")
            if user_selection == "deal":
                user_card.append(deal_card())
            elif user_selection == "stand":
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate(computer_card)

    print(f"  Final cards : {user_card}, final score : {user_score}")
    print(f"  Computer final's cards : {computer_card}, final score : {computer_score}")
    print(compare(user_score,computer_score))
    print("-----------------------------------------------------------------")

while input("Do you want to play another game? type 'Y' or 'N' : ").upper() == "Y":
    os.system('cls||clear')
    play_game()






