import pytest

from src import solution_one, solution_two


@pytest.fixture
def input():
    return """
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
    """


def test_solution_one(input):
    assert solution_one(input) == 24000


def test_solution_two(input):
    assert solution_two(input) == 45000
