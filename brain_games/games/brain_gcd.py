'''brain-gcd game logic'''

from random import randint


WELCOME_STRING = 'Find the greatest common divisor of given numbers.'
FIRST_ELEMENT_MIN = 1
FIRST_ELEMENT_MAX = 100


def get_gcd(num_min, num_max):
    return True if num_max % num_min == 0 else False


def get_sorted(a, b):
    '''Request tuple (a, b)
    Return tuple (min(a, b), max(a, b)
    '''
    if a > b:
        (a, b) = (b, a)
    return (a, b)


def game_set():
    a = randint(FIRST_ELEMENT_MIN, FIRST_ELEMENT_MAX)
    b = randint(FIRST_ELEMENT_MIN, FIRST_ELEMENT_MAX)
    data_to_show = '{0} {1}'.format(a, b)
    (a, b) = get_sorted(a, b)
    div = a
    while div > 0:
        if get_gcd(div, a) and get_gcd(div, b):
            correct_answer = str(div)
            break
        else:
            div -= 1
    return (data_to_show, correct_answer)
