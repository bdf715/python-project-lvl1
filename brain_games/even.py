"""Brain-games CLI."""

import prompt


def welcome_user():
    """Ask username, return greetings string."""
    name = prompt.string('May I have your name? ')
    return name


def check_even(number, answer):
    even = False
    odd = False
    correct_input = False
    if answer == 'yes' or answer == 'no':
        correct_input = True
    if number % 2 == 0:
        even = True
    else:
        odd = True
    if even and answer == 'yes' or odd and answer == 'no':
        return (True, answer)
    elif even and answer == 'no' or even and not correct_input:
        return (False, 'yes')
    elif odd and answer == 'yes' or odd and not correct_input:
        return (False, 'no')
