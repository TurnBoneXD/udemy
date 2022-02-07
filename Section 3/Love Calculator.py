# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_count = int(name1.lower().count("t"))+int(name2.lower().count("t"))+int(name1.lower().count("r"))+int(name2.lower().count("r"))+int(name1.lower().count("u"))+int(name2.lower().count("u"))+int(name1.lower().count("e"))+int(name2.lower().count("e"))
love_count = int(name1.lower().count("l"))+int(name2.lower().count("l"))+int(name1.lower().count("o"))+int(name2.lower().count("o"))+int(name1.lower().count("v"))+int(name2.lower().count("v"))+int(name1.lower().count("e"))+int(name2.lower().count("e"))
love_score = str(true_count)+str(love_count)


if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

