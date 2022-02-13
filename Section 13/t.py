import random       
import os
from this import s       #os.system('cls||clear')
from game_data import data
from art import logo,vs

#random data from game_data and add to above list
def random_data():
    first_data.append(random.choice(data))
    second_data.append(random.choice(data))

#return answer that have more follower (A or B) and amount of follower
def who_has_more_follower(first_data,second_data):
    compare_a = first_data[0]['follower_count'] 
    against_b = second_data[0]['follower_count'] 
    if compare_a > against_b:
        list_of_more_follower = ["A",compare_a]
        return first_data,list_of_more_follower
    elif compare_a < against_b:
        list_of_more_follower = ["B",against_b]
        return second_data,list_of_more_follower

first_data = []
second_data = []
random_data()


current_score = 0
more_follower = who_has_more_follower(first_data,second_data)
print(more_follower)


