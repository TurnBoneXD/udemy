import os
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

bids = {}

def find_highest_bid(bidding_record):
    highest = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest:
            highest = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}.")


bidding_finished = False
while not bidding_finished:
    name = input("Enter your name : ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    finished_or_not = input("Do you want to bid more? (Y/N) : ")
    if finished_or_not.upper() == "N":
        find_highest_bid(bids)
        bidding_finished = True
    elif finished_or_not.upper() == "Y":
        os.system('cls||clear')
