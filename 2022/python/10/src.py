from typing import Dict, List


def _get_cycles(commands: List) -> Dict:
    buffer, register_values = {}, {1: 1}
    x, idx = 1, 1
    for command in commands:
        x += buffer[idx] if idx in buffer.keys() else 0
        if command.startswith('addx'):
            buffer[idx+2] = int(command.split(' ')[-1])
            register_values[idx] = x
            idx += 1
        register_values[idx] = x
        idx += 1
    return register_values


def solution_one(input: str) -> int:
    input = input.split('\n')
    cycles = _get_cycles(input)
    return sum([key * value for key, value in cycles.items() if key in [20, 60, 100, 140, 180, 220]])


def solution_two(input: str) -> List:
    input = input.split('\n')
    cycles = _get_cycles(input)
    ctr = []
    for row in range(6):
        ctr_row = ''
        for col in range(40):
            cycle = row * 40 + col + 1
            ctr_row += '#' if abs(cycles[cycle] - col) <= 1 else '.'
        ctr.append(ctr_row)
    return ctr


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print("Solution 2:")
    for row in solution_two(input):
        print(row.replace('.', ' '))
