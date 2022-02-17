logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(random_card):
    return random.choice(random_card)

user_cards = []
computer_cards = []
user_cards.append(deal_card(cards))
computer_cards.append(deal_card(cards))

def calculate_score(card_list):
    if len(card_list) == 2 and sum(card_list) == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def blackjack():
    should_continue = True
    while should_continue:
        player_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {player_score}.")
        print(f"Dealer first cards: [{computer_cards[0]}], current score: {computer_score}.")
        if player_score == 0 or computer_score == 0 or player_score >21:
            print("Game end")
            should_continue = False
        else:
            if input("Do you want to draw another card? 'y' or 'n': ") == 'y':
                user_cards.append(deal_card(cards))
            else:
                print(f"Your final cards: {user_cards}, current score: {player_score}.")
                should_continue = False
                while computer_score < 17:
                    computer_cards.append(deal_card(cards))
                    computer_score = calculate_score(computer_cards)
                print(f"Dealer final cards: {computer_cards}, current score: {computer_score}.")
                
    def compare(plyr_score, comp_score):
        if plyr_score == comp_score:
            print("Its a Draw.")
        elif comp_score == 0:
            print("Player lost. Dealer got a black jack")
        elif plyr_score == 0:
            print("Player won. Player got a black jack")
        elif plyr_score > 21:
            print("Player lose. Player score is more than 21")
        elif comp_score > 21:
            print("Computer lose. Computer score is more than 21")
        else:
            if plyr_score > comp_score:
                print(f"Player won. Player has {plyr_score} and Dealer has {comp_score}")
            else:
                print(f"Computer won. Player has {plyr_score} and Dealer has {comp_score}")
    
    compare(player_score, computer_score)

blackjack()

if input("Do you want to restart the game? 'y' or 'n': ") == 'y':
    from os import system
    system("clear") # Clearing the screen
    print(logo)
    blackjack()
else:
    print("good bye.")