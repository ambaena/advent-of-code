from textwrap import dedent

import pytest

from src import solution_one, solution_two


def test_solution_one():
    input = dedent("""\
    R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2""")
    print(input)
    assert solution_one(input) == 13


def test_solution_two():
    input = dedent("""\
    R 5
    U 8
    L 8
    D 3
    R 17
    D 10
    L 25
    U 20""")
    assert solution_two(input) == 36
