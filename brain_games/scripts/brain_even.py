#!/usr/bin/env python

'''brain-even game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_even


def main():
    game_start(brain_even)


if __name__ == '__main__':
    main()
