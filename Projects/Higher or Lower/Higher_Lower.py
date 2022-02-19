import random
from game_data import data
from art import logo, vs
from os import system


def choose_celeb(data):
    """
    This function chooses a random celebrity from the data.
    """

    return random.choice(data)


def ask_question(A, B, vs):
    """
    This function asks the user if they think the celebrity is higher or lower.
    """

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}{vs}")
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
    answer = input(f'\nWhich is higher than other? "A" or "B": ')
    return answer


def compare_answer(A, B, user_answer):
    """
    This function compares the user's answer to the actual answer.
    """
    if user_answer == "A":
        if A["follower_count"] > B["follower_count"]:
            return True
        else:
            return False
    elif user_answer == "B":
        if A["follower_count"] < B["follower_count"]:
            return True
        else:
            return False
    else:
        print('Please enter "A" or "B"!')


def score_keeper(score_check, score):
    """
    This function keeps track of the score.
    """

    if score_check:
        return score + 1
    else:
        return score


def game():
    """
    This function runs the game.
    """

    should_continue = True
    A = choose_celeb(data)
    B = choose_celeb(data)
    if A == B:
        B = choose_celeb(data)
    score = 0
    while should_continue:
        print(logo)
        user_answer = ask_question(A, B, vs)
        score_check = compare_answer(A, B, user_answer)
        if score_check:
            score = score_keeper(score_check, score)
            B = choose_celeb(data)
            system("clear")
            print(f"You were Right!. Your score is {score}")
        else:
            print("You were wrong. Game Over!")
            should_continue = False


game()