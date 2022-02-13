import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo) # prints the logo

print(f'Pssst, the solution is {chosen_word}.')

display = [] # empty list
for _ in range(word_length):
    display += "_"

while not end_of_game: # While loop to keep the game running
    guess = input("Guess a letter: ").lower()

    if guess in display: # if the letter is already in the display, don't do anything 
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True # Set end of game to True if lives = 0
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives]) # Print hangman art based on their current lives