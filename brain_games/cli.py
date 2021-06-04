#!/usr/bin/env python

"""Brain-games CLI."""

import prompt


def welcome_user():
    """Ask username, return greetings string."""
    name = prompt.string('May I have your name? ')
    return 'Hello, {0}!'.format(name)


if __name__ == '__main__':
    print(welcome_user())
