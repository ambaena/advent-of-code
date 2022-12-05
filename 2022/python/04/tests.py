from textwrap import dedent

import pytest

from src import solution_one, solution_two


@pytest.fixture
def input():
    return dedent("""
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """)


def test_solution_one(input):
    assert solution_one(input) == 2


def test_solution_two(input):
    assert solution_two(input) == 4
