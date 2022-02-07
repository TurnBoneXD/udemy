print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10,12, or 15 ? "))
split = float(input("How many people to split the bill? "))

add_tip =  (tip/100) * total_bill + total_bill
split_pay = add_tip/ split
print("Each person should pay :" ,round(split_pay,2))