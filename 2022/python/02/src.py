from enum import Enum
import os
import sys


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


SHAPE = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSOR,
}

RULES = {
    (Shape.ROCK, Shape.ROCK): 3,
    (Shape.ROCK, Shape.PAPER): 0,
    (Shape.ROCK, Shape.SCISSOR): 6,
    (Shape.PAPER, Shape.PAPER): 3,
    (Shape.PAPER, Shape.SCISSOR): 0,
    (Shape.PAPER, Shape.ROCK): 6,
    (Shape.SCISSOR, Shape.SCISSOR): 3,
    (Shape.SCISSOR, Shape.ROCK): 0,
    (Shape.SCISSOR, Shape.PAPER): 6
}


def _translate_shape(shape: str) -> Shape:
    return SHAPE[{'X': 'A', 'Y': 'B', 'Z': 'C'}[shape]]


def _get_result(opponent: Shape, player: Shape) -> int:
    return player.value + RULES[(player, opponent)]


def _choose_shape(opponent: Shape, decision: str) -> Shape:
    if decision == 'Y':
        return opponent
    elif decision == 'X':
        return [key[0] for key, value in RULES.items() if value == 0 and key[1] == opponent][0]
    elif decision == 'Z':
        return [key[0] for key, value in RULES.items() if value == 6 and key[1] == opponent][0]


def solution_one(input: str) -> int:
    plays = input.strip().split('\n')
    return sum([_get_result(SHAPE[play[0]], _translate_shape(play[-1])) for play in plays])


def solution_two(input: str) -> int:
    plays = input.strip().split('\n')
    return sum([_get_result(SHAPE[play[0]], _choose_shape(SHAPE[play[0]], play[-1])) for play in plays])


if __name__ == "__main__":

    with open(os.path.join(sys.path[0], 'input'), 'r') as f:
        input = f.read()

    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
