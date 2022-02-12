
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

total = len(names)
payer = random.randint(0,total-1)
print(f"{names[payer]} is going to buy the meal today!")

''' 
Another way to do this is to use the random.choice() method.
'''
payer = random.choice(names)
print(f"{payer} is going to buy the meal today!")