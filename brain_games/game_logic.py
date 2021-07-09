'''Brain Games main logic module'''

from brain_games.cli import get_user_input


def game_greetings(game_module):
    user_question = 'May I have your name? '
    user_name = get_user_input(user_question)
    user_hello = 'Hello, {0}!'.format(user_name)
    game_hello = game_module.welcome_string()
    print('{0} \n {1}'.format(user_hello, game_hello))
    return (user_name, user_hello, game_hello)


def game_start(game_module):
    (user_name, user_hello, game_hello) = game_greetings(game_module)
    count = 0
    total_count = 3
    while count < total_count:
        data, correct_answer = game_module.game_set()
        print('Question: ' + data)
        user_question = 'Your answer: '
        user_answer = get_user_input(user_question)
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
