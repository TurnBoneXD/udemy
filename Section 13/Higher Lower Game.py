import random       
import os
from this import s       #os.system('cls||clear')
from game_data import data
from art import logo,vs

#random data from game_data and add to above list
def random_first_data():
    first_data.append(random.choice(data))

def random_second_data():
    second_data.append(random.choice(data))

#return answer that have more follower (A or B) and amount of follower
def who_has_more_follower(first_data,second_data):
    compare_a = first_data[0]['follower_count'] 
    against_b = second_data[0]['follower_count'] 
    if compare_a > against_b:
        list_of_more_follower = ["A",compare_a]
        return list_of_more_follower,first_data
    elif compare_a < against_b:
        list_of_more_follower = ["B",against_b]
        return list_of_more_follower,second_data

first_data = []
second_data = []
random_first_data()
current_score = 0
wrong_answer = False
print(logo)
while not wrong_answer:
    random_second_data()
    second_data = []
    more_follower = who_has_more_follower(first_data,second_data)

    print(f"Compare A: {first_data[0]['name']}, a {first_data[0]['description']}, from {first_data[0]['country']} ")
    print(vs)
    print(f"Against B: {second_data[0]['name']}, a {second_data[0]['description']}, from {second_data[0]['country']} ")

    print(more_follower)

    user_answer = input("Who has more followers,Type 'A' or 'B' : ").upper()
    if user_answer == more_follower[1][0]:
        os.system('cls||clear')
        print(f"You're right! Current score : {current_score+1}")
        first_data = more_follower[1]
    else:
        print(f"That's wrong! Your score is {current_score+0}")
        wrong_answer = True



