# 🚨 Don't change the code below 👇
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_amount = len(names)
random_index = random.randint(0,name_amount)
print(f"{names[random_index]} is going to but the meal today!")