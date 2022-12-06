import pytest

from src import solution_one, solution_two


@pytest.fixture
def input():
    return "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_solution_one(input):
    assert solution_one(input) == 7


def test_solution_two(input):
    assert solution_two(input) == 19
