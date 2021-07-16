"""brain-progression game logic"""

from random import randint


welcome_string = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    result = True
    div = n - 1
    while div in range(2, n):
        if n % div == 0:
            result = False
            break
        else:
            div -= 1
    return result


def game_set():
    n = randint(1, 100)
    data_to_show = str(n)
    correct_answer = 'yes' if is_prime(n) else 'no'
    return (data_to_show, correct_answer)
