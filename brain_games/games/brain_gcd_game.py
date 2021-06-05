"""brain-gcd game logic"""

from random import randint


def welcome_string():
    return 'Find the greatest common divisor of given numbers.'


def gcd(num_min, num_max):
    if num_max % num_min == 0:
        return True

def sort_tuple(a, b):
    '''Request tuple (a, b)
    Return tuple (min(a, b), max(a, b)
    '''
    if a > b:
        (a, b) = (b, a)
    return (a, b)


def game_set():
    a = randint(1, 100)
    b = randint(1, 100)
    data_to_show = '{0} {1}'.format(str(a), str(b))
    (a, b) = sort_tuple(a, b)    
    div = a
    while div > 0:
        if gcd(div, a) and gcd(div, b):
            correct_answer = str(div)
            break
        else:
            div -= 1
    return (data_to_show, correct_answer)
