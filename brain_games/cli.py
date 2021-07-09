"""Brain-games CLI."""

import prompt


def get_user_input(question):
    """Ask user for data, return user input"""
    user_input = prompt.string(question)
    return user_input
