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
game_images = [rock,paper,scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.randint(0,2)

if player_choice == 0:
	if player_choice == 0 and computer_choice == 0:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("Its a draw.")
	elif player_choice == 0 and computer_choice == 1:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("Computer Won.")
	elif player_choice == 0 and computer_choice == 2:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("You Won.")
elif player_choice == 1:
	if player_choice == 1 and computer_choice == 1:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("Its a draw.")
	elif player_choice == 1 and computer_choice == 0:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("You Won.")
	elif player_choice == 1 and computer_choice == 2:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("Computer Won.")
elif player_choice == 2:
	if player_choice == 2 and computer_choice == 2:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("Its a draw.")
	elif player_choice == 2 and computer_choice == 1:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("You Won.")
	elif player_choice == 2 and computer_choice == 0:
		print(f"You chose {game_images[player_choice]}")
		print(f"The computer chose {game_images[computer_choice]}")
		print("Computer Won.")
else:
	print("Wrong Input")

