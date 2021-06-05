"""brain-gcd game logic"""

from random import randint


def welcome_string():
    return 'Find the greatest common divisor of given numbers.'


def gcd(num_min, num_max):
    if num_max % num_min == 0:
        return True


def game_set():
    a = randint(1, 100)
    b = randint(1, 100)
    data_to_show = '{0} {1}'.format(str(a), str(b))
    if a > b:
        (a, b) = (b, a)
    div = a
    while div > 0:
        if gcd(div, a) and gcd(div, b):
            correct_answer = str(div)
            break
        else:
            div -= 1
    return (data_to_show, correct_answer)
