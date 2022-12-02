from textwrap import dedent

import pytest

from src import solution_one, solution_two


@pytest.fixture
def input():
    return dedent("""
    A Y
    B X
    C Z""")


def test_solution_one(input):
    assert solution_one(input) == 15


def test_solution_two(input):
    assert solution_two(input) == 12
