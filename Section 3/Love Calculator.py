# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_count = int(name1.count("t"))+int(name2.count("t"))+int(name1.count("r"))+int(name2.count("r"))+int(name1.count("u"))+int(name2.count("u"))+int(name1.count("e"))+int(name2.count("e"))
love_count = int(name1.count("l"))+int(name2.count("l"))+int(name1.count("o"))+int(name2.count("o"))+int(name1.count("v"))+int(name2.count("v"))+int(name1.count("e"))+int(name2.count("e"))
love_score = str(true_count)+str(love_count)


if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")