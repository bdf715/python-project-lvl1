#!/usr/bin/env python

'''brain-calc game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_calc


def main():
    game_module = brain_calc
    game_start(game_module)


if __name__ == '__main__':
    main()
