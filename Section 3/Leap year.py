print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")



if size == "S":
    total_price = 15
    if add_pepperoni.upper() == "y" :
        total_price += 2
    elif add_pepperoni.upper() == "n" :
        total_price += 0
    elif extra_cheese.upper() == "y":
        total_price += 1       
    elif extra_cheese.upper() == "n":
        total_price += 0
print("Your final bill is :",total_price)

if size == "M":
    total_price = 20
    if add_pepperoni.upper() == "y" :
        total_price += 3
    elif add_pepperoni.upper() == "n" :
        total_price += 0
    elif extra_cheese.upper() == "y":
        total_price += 1       
    elif extra_cheese.upper() == "n":
        total_price += 0
print("Your final bill is :",total_price)

if size == "M":
    total_price = 25
    if add_pepperoni.upper() == "y" :
        total_price += 3
    elif add_pepperoni.upper() == "n" :
        total_price += 0
    elif extra_cheese.upper() == "y":
        total_price += 1       
    elif extra_cheese.upper() == "n":
        total_price += 0
print("Your final bill is :",total_price)




    

    

