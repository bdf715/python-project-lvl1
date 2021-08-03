'''brain-progression game logic'''

from random import randint


WELCOME_STRING = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_ELEMENT_MIN = 1
FIRST_ELEMENT_MAX = 100


def is_prime(n):
    result = True
    div = n - 1
    while div in range(2, n):
        if n % div == 0:
            return False
        else:
            div -= 1
    return result


def game_set():
    n = randint(FIRST_ELEMENT_MIN, FIRST_ELEMENT_MAX)
    data_to_show = str(n)
    correct_answer = 'yes' if is_prime(n) else 'no'
    return (data_to_show, correct_answer)
