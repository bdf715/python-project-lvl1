"""Brain-games CLI."""

import prompt


def get_user_input(question):
    """Ask user for data, return user input"""
    user_input = prompt.string(question)
    return user_input


def welcome_user():
    """Ask username, return greetings string."""
    name = prompt.string('May I have your name? ')
    return 'Hello, {0}!'.format(name)
