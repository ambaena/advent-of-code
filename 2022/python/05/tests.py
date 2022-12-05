import pytest

from src import solution_one, solution_two


@pytest.fixture
def input():
    return open('input_tests').read()


def test_solution_one(input):
    assert solution_one(input) == 'CMZ'


def test_solution_two(input):
    assert solution_two(input) == 'MCD'
