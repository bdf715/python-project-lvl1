#!/usr/bin/env python

'''brain-calc game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_calc_game


def main():
    game_module = brain_calc_game
    game_start(game_module)


if __name__ == '__main__':
    main()
