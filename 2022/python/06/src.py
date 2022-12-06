def _get_market_after_n_consecutive_chars(buffer: str, n: int) -> int:
    for idx in range(len(buffer) - (n-1)):
        if len(set(buffer[idx:idx+n])) == n:
            return idx + n


def solution_one(input: str) -> str:
    return _get_market_after_n_consecutive_chars(input, 4)


def solution_two(input: str) -> str:
    return _get_market_after_n_consecutive_chars(input, 14)


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
