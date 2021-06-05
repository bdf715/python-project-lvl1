'''brain-calc game logic'''

from random import randint, choice


def welcome_string():
    return 'What is the result of the expression?'


def game_set():
    a = randint(1, 100)
    b = randint(1, 100)
    sign = choice(['+', '-', '*'])
    data_to_show = '{0} {1} {2}'.format(str(a), sign, str(b))
    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b
    elif sign == '*':
        result = a * b
    correct_answer = str(result)
    return (data_to_show, correct_answer)
