#!/usr/bin/env python

"""Docstring."""

from brain_games.even import welcome_user, check_even

print('Welcome to the Brain Games!')
name = welcome_user()
print("Hello, {0}!".format(name))
print('Answer "yes" if the number is even, otherwise answer "no".')
count = 0
while count < 3:
    if check_even():
        print("Correct!")
        count += 1
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'." + "\n" \
                + "Let's try again, " + name + "!")
        break
print("Congratulations, {0}!".format(name))
        


