"""brain-even game logic"""

from random import randint

def welcome_string():
    return 'Answer "yes" if the number is even, otherwise answer "no".'

def game_set():
    number = randint(1,100)
    data_to_show = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (data_to_show, correct_answer)


def game_check(user_answer, correct_answer):
    if user_answer == correct_answer:
        return (True, user_answer)
    else:
        return (False, correct_answer)