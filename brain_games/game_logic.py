'''Brain Games main logic module'''

import prompt
from brain_games.games import brain_calc_game
from brain_games.games import brain_even_game
from brain_games.games import brain_gcd_game
from brain_games.games import brain_progression_game
from brain_games.games import brain_prime_game


def games(game_name):
    if game_name == 'brain-calc':
        used_module = brain_calc_game
    elif game_name == 'brain-even':
        used_module = brain_even_game
    elif game_name == 'brain-gcd':
        used_module = brain_gcd_game
    elif game_name == 'brain-progression':
        used_module = brain_progression_game
    elif game_name == 'brain-prime':
        used_module = brain_prime_game
    return used_module


def game_greetings(game_name):
    user_name = prompt.string('May I have your name? ')
    user_hello = 'Hello, {0}!'.format(user_name)
    game_hello = games(game_name).welcome_string()
    print('{0} \n {1}'.format(user_hello, game_hello))
    return (user_name, user_hello, game_hello)


def game_start(game_name):
    (user_name, user_hello, game_hello) = game_greetings(game_name)
    count = 0
    while count < 3:
        data, correct_answer = games(game_name).game_set()
        print('Question: ' + data)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print('{0} is wrong answer ;(. Correct answer was \
{1}.'.format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
    else:
        print('Congratulations, {0}!'.format(user_name))
