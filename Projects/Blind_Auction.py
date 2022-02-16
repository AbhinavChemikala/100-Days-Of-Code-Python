logo = '''
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
'''
print(logo)
print("Welcome to secret auction program.")
auction = {}
end_of_game = True
from os import system

def find_highest_bid(auction): # Find the highest bid in the auction
    highest_bidder = max(auction) # Finding the highest bidder using the max() function
    highest_bid = auction[highest_bidder] # Finding the highest bid
    print(f"The highest bidder is {highest_bidder} with ${highest_bid}.")


while end_of_game:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    auction[name] = bid
    cont = input("Are there any bidders? type 'yes' or 'no': ").lower()
    system("clear") # Clearing the screen
    if cont == 'no':
        end_of_game = False
        find_highest_bid(auction) # Calling the function


