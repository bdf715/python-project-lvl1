'''brain-even game logic'''

from random import randint


welcome_string = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def game_set():
    number = randint(1, 100)
    data_to_show = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return (data_to_show, correct_answer)
