ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
PRIORITIES = {char:ALPHABET.index(char)+1 for char in ALPHABET}


def _get_item_between_comparments(rucksack: str):
    sep = int(len(rucksack)/2)
    return set(item for item in rucksack[:sep] if item in rucksack[sep:]).pop()


def _get_item_between_three_rucksacks(rucksack_one: str, rucksack_two: str, rucksack_three: str):
    return set(item for item in rucksack_one if item in rucksack_two and item in rucksack_three).pop()


def solution_one(input: str) -> int:
    rucksacks = input.strip().split('\n')
    return sum([PRIORITIES[_get_item_between_comparments(rucksack)] for rucksack in rucksacks])


def solution_two(input: str) -> int:
    rucksacks = input.strip().split('\n')
    return sum([PRIORITIES[_get_item_between_three_rucksacks(rucksacks[idx], rucksacks[idx+1], rucksacks[idx+2])] for idx in range(len(rucksacks)) if idx % 3 == 0])


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
