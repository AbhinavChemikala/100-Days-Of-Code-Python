import random
logo = """
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def guess_number():
    """Returns a random number between 1 and 100."""
    guess = random.randint(1,100)
    return guess

def choose_difficulty():
    """Returns a difficulty level."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
        
    return lives

main_number = guess_number()
user_lives = choose_difficulty()
print(f"pstt the answer is {main_number}")

should_continue = True
while should_continue and user_lives > 0:
    print(f"You have {user_lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == main_number:
        print(f"You got it! The answer was {main_number}.")
        should_continue = False
    elif user_guess < main_number:
        user_lives -= 1
        print("Too low.")
        print("Guess again.")
    else:
        user_lives -= 1
        print("Too high.")
        print("Guess again.")

if user_lives == 0:
    print("You've run out of guesses, you lose.")