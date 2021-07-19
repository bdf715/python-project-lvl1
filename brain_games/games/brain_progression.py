'''brain-progression game logic'''

from random import randint


welcome_string = 'What number is missing in the progression?'
length_min = 5
length_max = 10
first_element_min = 5
first_element_max = 15
delta_min = 5
delta_max = 15


def get_progression():
    length = randint(length_min, length_max)
    first_element = randint(first_element_min, first_element_max)
    delta = randint(delta_min, delta_max)
    progression = []
    for step in range(0, length):
        element = first_element + delta * step
        progression.append(str(element))
    return progression


def game_set():
    progression = get_progression()
    random_index = randint(0, len(progression) - 1)
    random_element = progression[random_index]
    progression[random_index] = '..'
    data_to_show = ' '.join(progression)
    correct_answer = str(random_element)
    return (data_to_show, correct_answer)
