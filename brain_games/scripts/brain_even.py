#!/usr/bin/env python

from random import randint
import prompt
from brain_games.even import welcome_user, check_even

"""Docstring."""


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print("Hello, {0}!".format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        (even, correct_answer) = check_even(number, answer)
        if even:
            print("Correct!")
            count += 1
            if count == 3:
                print("Congratulations, {0}!".format(name))
        else:
            print("'{0}' is wrong answer ;(. Correct answer was \
'{1}'.".format(answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            break


if __name__ == '__main__':
    main()
