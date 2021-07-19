'''brain-calc game logic'''

from random import randint, choice


WELCOME_STRING = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']


def get_calculation(a, sign, b):
    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b
    elif sign == '*':
        result = a * b
    return result


def game_set():
    a = randint(1, 100)
    b = randint(1, 100)
    sign = choice(OPERATIONS)
    data_to_show = '{0} {1} {2}'.format(a, sign, b)
    correct_answer = str(get_calculation(a, sign, b))
    return (data_to_show, correct_answer)
