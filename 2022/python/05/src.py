from typing import List


def _get_stacks(input_head: str) -> List:
    num_stacks = len(input_head.split('\n')[-1].split('   '))
    stacks = []
    for stack_idx in range(1, num_stacks*3 + num_stacks-1, 4):
        stacks.append([row[stack_idx] for row in input_head.split('\n')[-2::-1] if row[stack_idx] != ' '])
    return stacks


def _apply_rules(stacks: List, rules: str, crane: str = '9000') -> None:
    for rule in rules.split('\n'):
        move, initial_stack, end_stack = int(rule.split(' ')[1]), int(rule.split(' ')[3]) - 1, int(rule.split(' ')[-1]) - 1
        stack_to_move = stacks[initial_stack][-move:] if crane == '9001' else stacks[initial_stack][-move:][::-1]
        stacks[end_stack] += stack_to_move
        stacks[initial_stack] = stacks[initial_stack][:-move]


def solution_one(input: str) -> str:
    stacks = _get_stacks(input.split('\n\n')[0])
    _apply_rules(stacks=stacks, rules=input.split('\n\n')[-1])
    return ''.join([stack[-1] for stack in stacks])


def solution_two(input: str) -> str:
    stacks = _get_stacks(input.split('\n\n')[0])
    _apply_rules(stacks=stacks, rules=input.split('\n\n')[-1], crane='9001')
    return ''.join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
