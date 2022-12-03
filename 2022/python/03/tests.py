from textwrap import dedent

import pytest

from src import solution_one, solution_two


@pytest.fixture
def input():
    return dedent("""
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """)


def test_solution_one(input):
    assert solution_one(input) == 157


def test_solution_two(input):
    assert solution_two(input) == 70
