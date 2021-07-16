#!/usr/bin/env python

'''brain-even game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_even


def main():
    game_module = brain_even
    game_start(game_module)


if __name__ == '__main__':
    main()
