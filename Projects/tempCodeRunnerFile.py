import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player = [rock,paper,scissors]
computer = [rock,paper,scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0,2)
print(computer_choice)

if player_choice == 0:
	if player_choice == 0 and computer_choice == 0:
		print(player[0])
		print(computer[0])
		print("Its a draw.")
	elif player_choice == 0 and computer_choice == 1:
		print(player[0])
		print(computer[1])
		print("Computer Won.")
	elif player_choice == 0 and computer_choice == 2:
		print(player[0])
		print(computer[2])
		print("You Won.")
elif player_choice == 1:
	if player_choice == 1 and computer_choice == 1:
		print(player[1])
		print(computer[1])
		print("Its a draw.")
	elif player_choice == 1 and computer_choice == 0:
		print(player[1])
		print(computer[0])
		print("You Won.")
	elif player_choice == 1 and computer_choice == 2:
		print(player[1])
		print(computer[2])
		print("Computer Won.")
elif player_choice == 2:
	if player_choice == 2 and computer_choice == 2:
		print(player[2])
		print(computer[2])
		print("Its a draw.")
	elif player_choice == 2 and computer_choice == 1:
		print(player[2])
		print(computer[1])
		print("You Won.")
	elif player_choice == 2 and computer_choice == 0:
		print(player[2])
		print(computer[0])
		print("Computer Won.")
else:
	print("Wrong Input")

