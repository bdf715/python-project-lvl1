"""brain-progression game logic"""

from random import randint


def welcome_string():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_set():
    n = randint(1, 100)
    data_to_show = str(n)
    correct_answer = 'yes'
    div = n - 1
    while div in range(2, n + 1):
        if n % div == 0:
            correct_answer = 'no'
            break
        else:
            div -= 1
    return (data_to_show, correct_answer)
