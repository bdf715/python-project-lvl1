'''brain-gcd game logic'''

from random import randint
from math import gcd


WELCOME_STRING = 'Find the greatest common divisor of given numbers.'
FIRST_ELEMENT_MIN = 1
FIRST_ELEMENT_MAX = 100


def game_set():
    a = randint(FIRST_ELEMENT_MIN, FIRST_ELEMENT_MAX)
    b = randint(FIRST_ELEMENT_MIN, FIRST_ELEMENT_MAX)
    data_to_show = '{0} {1}'.format(a, b)
    correct_answer = str(gcd(a, b))
    return (data_to_show, correct_answer)
