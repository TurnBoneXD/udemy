# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_price = 0

if size.upper() == "S":
    total_price = 15
    if add_pepperoni.upper() == "Y" :
        total_price += 2
    if extra_cheese.upper() == "Y" :
        total_price +=1
    print(f"Your final bill is : $ {total_price}")
elif size.upper() == "M":
    total_price = 20
    if add_pepperoni.upper() == "Y" :
        total_price += 3
    if extra_cheese.upper() == "Y" :
        total_price +=1
    print(f"Your final bill is : ${total_price}")
elif size.upper() == "L":
    total_price = 25
    if add_pepperoni.upper() == "Y" :
        total_price += 3
    if extra_cheese.upper() == "Y" :
        total_price +=1
    print(f"Your final bill is : ${total_price}")








    

    

