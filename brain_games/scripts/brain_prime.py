#!/usr/bin/env python

'''brain-prime game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_prime


def main():
    game_start(brain_prime)


if __name__ == '__main__':
    main()
