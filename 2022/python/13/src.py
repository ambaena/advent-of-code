def _is_ordered(left, right) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right
    elif isinstance(left, list) and isinstance(right, list):
        for idx in range(min(len(left), len(right))):
            if (is_ordered := _is_ordered(left[idx], right[idx])) is not None:
                return is_ordered
        return _is_ordered(len(left), len(right))
    else:
        return _is_ordered(left if isinstance(left, list) else [left], right if isinstance(right, list) else [right])


def solution_one(input: str) -> int:
    pairs = [(eval(pair.split('\n')[0]), eval(pair.split('\n')[1])) for pair in input.split('\n\n')]
    return sum([idx for idx, pair in enumerate(pairs, start=1) if _is_ordered(pair[0], pair[1])])


def solution_two(input: str) -> int:
    packets = [eval(packet) for pair in input.split('\n\n') for packet in pair.split('\n')]
    first_divisor_idx = sum([1 for packet in packets if _is_ordered(packet, [[2]])]) + 1
    second_divisor_idx = sum([1 for packet in packets if _is_ordered(packet, [[6]])]) + 2
    return first_divisor_idx * second_divisor_idx


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
