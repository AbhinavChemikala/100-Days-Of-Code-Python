#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percent = input("What tip percentage would you like to give? 10, 12, 15? ")
split_num = input("How many people to split the bill? ")
tip_percent = (int(tip_percent) / 100 + 1)
tip = float(total_bill) * tip_percent
single_total = tip / int(split_num) 
print(f"Each person should pay: ${single_total:.2f}") # :.2f is the format for 2 decimal places