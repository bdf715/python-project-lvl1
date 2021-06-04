"""Brain-games CLI."""

import prompt


def welcome_user():
    """Ask username, return greetings string."""
    name = prompt.string('May I have your name? ')
    return name

def check_even():
    number = prompt.string('Question: ') 
    try:
        if number % 2 == 0:
            return True
        else:
            return False
        except TypeError:
            return False
