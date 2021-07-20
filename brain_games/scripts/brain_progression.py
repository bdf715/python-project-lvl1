#!/usr/bin/env python

'''brain-progression game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_progression


def main():
    game_start(brain_progression)


if __name__ == '__main__':
    main()
