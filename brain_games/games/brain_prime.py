"""brain-progression game logic"""

from random import randint


welcome_string = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_not_prime(n, div):
    return True if n % div == 0 else False


def game_set():
    n = randint(1, 100)
    data_to_show = str(n)
    correct_answer = 'yes'
    div = n - 1
    while div in range(2, n + 1):
        if is_not_prime(n, div):
            correct_answer = 'no'
            break
        else:
            div -= 1
    return (data_to_show, correct_answer)
