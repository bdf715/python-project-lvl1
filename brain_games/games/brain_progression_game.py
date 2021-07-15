'''brain-progression game logic'''

from random import randint


welcome_string = 'What number is missing in the progression?'


def get_progression():
    length = randint(5, 15)
    start = randint(5, 15)
    delta = randint(5, 15)
    progression = []
    for step in range(0, length):
        element = start + delta * step
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
