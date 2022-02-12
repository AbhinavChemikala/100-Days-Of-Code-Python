print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


count1 = 0
count2 = 0
full_name = name1.lower() + name2.lower()

count1+= full_name.count("t")
count1+= full_name.count("r")
count1+= full_name.count("u")
count1+= full_name.count("e")
count2+= full_name.count("l")
count2+= full_name.count("o")
count2+= full_name.count("v")
count2+= full_name.count("e")

score = int(str(count1) + str(count2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}."
)
