import random
import os
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21: #[11,11] >>> [11,1] 
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: #for user
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'Draw' to get another card, type 'Stand' to pass: ").lower()
            print("-----------------------------------------------------------------")
            if user_should_deal == "draw":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17: #for computer
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final's hand: {user_cards}, final score: {user_score}")
    print(f"    Computer final's hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))
    print("-----------------------------------------------------------------")

while input("Do you want to play a game of Blackjack? Type 'Y' or 'N' : ").upper() == "Y":
    os.system('cls||clear')
    play_blackjack()





