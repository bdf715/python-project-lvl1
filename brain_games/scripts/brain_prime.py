#!/usr/bin/env python

'''brain-prime game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_prime


def main():
    game_module = brain_prime
    game_start(game_module)


if __name__ == '__main__':
    main()
