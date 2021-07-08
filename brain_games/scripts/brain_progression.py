#!/usr/bin/env python

'''brain-progression game script'''

from brain_games.game_logic import game_start
from brain_games.games import brain_progression_game


def main():
    game_module = brain_progression_game
    game_start(game_module)


if __name__ == '__main__':
    main()
