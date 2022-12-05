def _are_overlapped(section_one: str, section_two: str, how: str = 'all') -> bool:
    section_one = list(range(int(section_one.split('-')[0]), int(section_one.split('-')[-1]) + 1))
    section_two = list(range(int(section_two.split('-')[0]), int(section_two.split('-')[-1]) + 1))
    if how == 'all':
        return all(item_one in section_two for item_one in section_one) or all(item_two in section_one for item_two in section_two)
    elif how == 'any':
        return any(item_one in section_two for item_one in section_one) or any(item_two in section_one for item_two in section_two)


def solution_one(input: str) -> int:
    elfs_pair = [elfs_pair.split(',') for elfs_pair in input.strip().split('\n')]
    return sum([1 for pair in elfs_pair if _are_overlapped(pair[0], pair[-1])])


def solution_two(input: str) -> int:
    elfs_pair = [elfs_pair.split(',') for elfs_pair in input.strip().split('\n')]
    return sum([1 for pair in elfs_pair if _are_overlapped(pair[0], pair[-1], how='any')])


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
