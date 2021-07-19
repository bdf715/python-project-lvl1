'''brain-even game logic'''

from random import randint


WELCOME_STRING = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_ELEMENT_MIN = 1
FIRST_ELEMENT_MAX = 100


def is_even(number):
    return True if number % 2 == 0 else False


def game_set():
    number = randint(FIRST_ELEMENT_MIN, FIRST_ELEMENT_MAX)
    data_to_show = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return (data_to_show, correct_answer)
