import os
import sys


def _get_elf_total_calories(input: str):
    return [sum(map(int, elf.split('\n'))) for elf in input.strip().split('\n\n')]


def solution_one(input: str) -> int:
    return max(_get_elf_total_calories(input))


def solution_two(input: str) -> int:
    elfs = _get_elf_total_calories(input)
    elfs.sort()
    return sum(elfs[-3:])


if __name__ == "__main__":

    with open(os.path.join(sys.path[0], 'input'), 'r') as f:
        input = f.read()

    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
