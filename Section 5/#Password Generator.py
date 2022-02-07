import random

letter_list = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
number_list = ["0","1","2","3","4","5","6","7","8","9"]
symbol_list = ["!","@","#","$","%","&","*","(",")"]

letter_input = int(input("How many letters would you like?\n"))
number_input = int(input("How many numbers would you like?\n"))
symbol_input = int(input("How many symbols would you like?\n"))

password_not_rand = []
for lround in range(letter_input):
    password_not_rand.append(random.choice(letter_list))

for nround in range(number_input):
    password_not_rand.append(random.choice(number_list))

for sround in range(symbol_input):
    password_not_rand.append(random.choice(symbol_list))


random.shuffle(password_not_rand)

password_random_again = ""
for char in password_not_rand:
    password_random_again += char

print(f"Your password is {password_random_again}")


'''
password_new = ""
for i in range(len(password_not_rand)):
    r = random.choice(password_not_rand)
    password_new += r
    password_not_rand.remove(r)

print(f"Your password is {password_new}")
'''