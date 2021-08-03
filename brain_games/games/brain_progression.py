'''brain-progression game logic'''

from random import randint


WELCOME_STRING = 'What number is missing in the progression?'
LENGTH_MIN = 5
LENGTH_MAX = 10
FIRST_ELEMENT_MIN = 5
FIRST_ELEMENT_MAX = 15
DELTA_MIN = 5
DELTA_MAX = 15


def get_progression(first_element, delta, length):
    progression = []
    for step in range(0, length):
        element = first_element + delta * step
        progression.append(str(element))
    return progression


def game_set():
    length = randint(LENGTH_MIN, LENGTH_MAX)
    first_element = randint(FIRST_ELEMENT_MIN, FIRST_ELEMENT_MAX)
    delta = randint(DELTA_MIN, DELTA_MAX)
    progression = get_progression(first_element, delta, length)
    random_index = randint(0, len(progression) - 1)
    random_element = progression[random_index]
    progression[random_index] = '..'
    data_to_show = ' '.join(progression)
    correct_answer = str(random_element)
    return (data_to_show, correct_answer)
