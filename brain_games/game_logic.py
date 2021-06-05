'''Brain Games main logic module'''

import prompt
from brain_games.games import brain_calc_game
from brain_games.games import brain_even_game


def welcome_user():
    """Ask username, return greetings string."""
    name = prompt.string('May I have your name? ')
    return name


def games(game_name):
    if game_name == 'brain-calc':
        return brain_calc_game
    elif game_name == 'brain-even':
        return brain_even_game
        '''if function == 'welcome':
            return brain_calc_game.welcome_string()
        elif function == 'set':
            return brain_calc_game.game_set()
        elif function == 'check':
            return brain_calc_game.game_check()
        '''


def game_start(game_name):
    user_name = prompt.string('May I have your name? ')
    print("Hello, {0}!".format(user_name))
    print(games(game_name).welcome_string())
    count = 0
    while count < 3:
        data, correct_answer = games(game_name).game_set()
        print('Question: ' + data)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print("Congratulations, {0}!".format(user_name))
        else:
            print("'{0}' is wrong answer ;(. Correct answer was \
'{1}'.".format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
