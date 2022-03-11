MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

in_machine = {
    "water":300, #300
    "milk":200, #200
    "coffee":100, #100
    "money":0
}

def user_money():
    total_user_money = 0
    print("Plese insert coins.")
    quarters = float(input("How many quarters? : "))
    dimes = float(input("How many dimes? : "))
    nickles = float(input("How many nickles? : "))
    pennies = float(input("How many pennies? : "))
    total_user_money += (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return float(total_user_money)

def check_indredient(no_type,coffee_type):
    if in_machine["coffee"] < MENU[coffee_type]["ingredients"]["coffee"] and in_machine["water"] < MENU["espresso"]["ingredients"]["water"] and in_machine["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        no_type = "Sorry there is not enough water, coffee and milk."
    elif in_machine["coffee"] < MENU[coffee_type]["ingredients"]["coffee"] and in_machine["water"] < MENU["espresso"]["ingredients"]["water"]:
        no_type = "Sorry there is not enough water and coffee."
    elif in_machine["milk"] < MENU[coffee_type]["ingredients"]["milk"] and in_machine["water"] < MENU["espresso"]["ingredients"]["water"]:
        no_type = "Sorry there is not enough milk and water." 
    elif in_machine["coffee"] < MENU[coffee_type]["ingredients"]["coffee"] and in_machine["milk"] < MENU["espresso"]["ingredients"]["milk"]:
        no_type = "Sorry there is not enough milk and coffee."     
    elif in_machine["water"] < MENU[coffee_type]["ingredients"]["water"] :
        no_type = "Sorry there is not enough water."
    elif in_machine["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        no_type = "Sorry there is not enough coffee."
    elif in_machine["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        no_type = "Sorry there is not enough milk."
    return no_type

def espresso(total_user_money):  
    if total_user_money < 1.5:
        return "Sorry that's not enough money. Money refunded."
    elif total_user_money >= 1.5:
        in_machine["water"] = in_machine["water"]-MENU["espresso"]["ingredients"]["water"]
        in_machine["coffee"] = in_machine["coffee"]-MENU["espresso"]["ingredients"]["coffee"]
        in_machine["milk"] = in_machine["milk"]-MENU["espresso"]["ingredients"]["milk"]
        in_machine["money"] = in_machine["money"]+MENU["espresso"]["cost"]
        change = round(total_user_money-1.5,2)
        return f"Here is ${change} in change"

def latte(total_user_money):  
    if total_user_money < 2.5:
        return "Sorry that's not enough money. Money refunded."
    elif total_user_money >= 2.5:
        in_machine["water"] = in_machine["water"]-MENU["latte"]["ingredients"]["water"]
        in_machine["coffee"] = in_machine["coffee"]-MENU["latte"]["ingredients"]["coffee"]
        in_machine["milk"] = in_machine["milk"]-MENU["latte"]["ingredients"]["milk"]
        in_machine["money"] = in_machine["money"]+MENU["latte"]["cost"]
        change = round(total_user_money-1.5,2)
        return f"Here is ${change} in change"
    
def cappuccino(total_user_money):  
    if total_user_money < 3:
        return "Sorry that's not enough money. Money refunded."
    elif total_user_money >= 3:
        in_machine["water"] = in_machine["water"]-MENU["cappuccino"]["ingredients"]["water"]
        in_machine["coffee"] = in_machine["coffee"]-MENU["cappuccino"]["ingredients"]["coffee"]
        in_machine["milk"] = in_machine["milk"]-MENU["cappuccino"]["ingredients"]["milk"]
        in_machine["money"] = in_machine["money"]+MENU["cappuccino"]["cost"]
        change = round(total_user_money-1.5,2)
        return f"Here is ${change} in change"
    
    
is_machine_off = False
while not is_machine_off:
    user_choose = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choose == "espresso":
        no_type = ""
        if "Sorry" in check_indredient(no_type,user_choose):
            print(check_indredient(no_type,user_choose))
        elif "Sorry" not in check_indredient(no_type,user_choose):
            total_user_money = user_money()
            print(espresso(total_user_money))
            if total_user_money >= 1.5 :
                print("Here is your espresso. Enjoy!")

    elif user_choose == "latte":
        no_type = ""
        if "Sorry" in check_indredient(no_type,user_choose):
            print(check_indredient(no_type,user_choose))
        elif "Sorry" not in check_indredient(no_type,user_choose):
            total_user_money = user_money()
            print(latte(total_user_money))
            if total_user_money >= 2.5 :
                print("Here is your latte. Enjoy!")
    
    elif user_choose == "cappuccino":
        no_type = ""
        if "Sorry" in check_indredient(no_type,user_choose):
            print(check_indredient(no_type,user_choose))
        elif "Sorry" not in check_indredient(no_type,user_choose):
            total_user_money = user_money()
            print(cappuccino(total_user_money))
            if total_user_money >= 3 :
                print("Here is your cappuccino. Enjoy!")
    
    elif user_choose == "report":
        water = in_machine["water"]
        milk = in_machine["milk"]
        coffee = in_machine["coffee"]
        money = in_machine["money"]
        print(f"Water : {water}ml")
        print(f"Milk : {milk}ml")
        print(f"Coffee : {coffee}g")
        print(f"money : ${money}")

    elif user_choose == "off":
        is_machine_off = True



