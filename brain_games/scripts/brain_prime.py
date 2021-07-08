#!/usr/bin/env python

'''brain-prime game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_prime_game


def main():
    game_module = brain_prime_game
    game_start(game_module)


if __name__ == '__main__':
    main()
