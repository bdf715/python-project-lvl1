'''brain-progression game logic'''

from random import randint


def welcome_string():
    return 'What number is missing in the progression?'


def game_set():
    progr_length = randint(5, 15)
    progr_start = randint(1, 50)
    progr_delta = randint(1, 9)
    progr = []
    n = progr_start
    while len(progr) <= progr_length:
        progr.append(str(n))
        n += progr_delta
    random_index = randint(0, progr_length - 1)
    random_element = progr[random_index]
    progr[random_index] = '..'
    data_to_show = ' '.join(progr)
    correct_answer = str(random_element)
    return (data_to_show, correct_answer)
