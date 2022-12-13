from dataclasses import dataclass
from typing import Callable, List
import re


@dataclass
class Monkey():
    num: int
    items: List
    operation: Callable
    test_divisor: int
    test: Callable
    throw_to_true: int
    throw_to_false: int
    inspected_items: int = 0

    def receive_item(self, item):
        self.items.append(item)


def _parse_input(input: List) -> List[Monkey]:
    monkey_list = []
    for monkey in input:
        monkey_attrs = monkey.split('\n')
        num = int(re.findall(r'\d+', monkey_attrs[0])[0])
        starting_items = re.findall(r'\d+', monkey_attrs[1])
        operation = eval(f'lambda old: {monkey_attrs[2].split(" = ")[-1]}')
        test_divisor = int(monkey_attrs[3].split(" ")[-1])
        test = eval(f'lambda item: item % {monkey_attrs[3].split(" ")[-1]} == 0')
        throw_to_true = int(re.findall(r'\d+', monkey_attrs[4])[0])
        throw_to_false = int(re.findall(r'\d+', monkey_attrs[5])[0])
        monkey_list.append(Monkey(num, starting_items, operation, test_divisor, test, throw_to_true, throw_to_false, 0))
    return monkey_list


def solution_one(input: str) -> int:
    monkeys = _parse_input(input.split('\n\n'))
    thrown_items = []
    for _ in range(20):
        for monkey in monkeys:
            for to_monkey, item in thrown_items.copy():
                if to_monkey == monkey.num:
                    thrown_items.remove((to_monkey, item))
                    monkey.receive_item(item)
            for item in monkey.items:
                worry_level = int(int(monkey.operation(int(item))) / 3)
                if monkey.test(worry_level):
                    thrown_items.append((monkey.throw_to_true, worry_level))
                else:
                    thrown_items.append((monkey.throw_to_false, worry_level))
                monkey.inspected_items += 1
            monkey.items = []

    monkey_bussines = sorted([monkey.inspected_items for monkey in monkeys])
    return monkey_bussines[-1] * monkey_bussines[-2]


def solution_two(input: str) -> int:
    monkeys = _parse_input(input.split('\n\n'))
    mul, thrown_items = 1, []

    for monkey in monkeys:
        mul *= monkey.test_divisor
    for _ in range(10000):
        for monkey in monkeys:
            for to_monkey, item in thrown_items.copy():
                if to_monkey == monkey.num:
                    thrown_items.remove((to_monkey, item))
                    monkey.receive_item(item)
            for item in monkey.items:
                worry_level = int(int(monkey.operation(int(item))) % mul)
                if monkey.test(worry_level):
                    thrown_items.append((monkey.throw_to_true, worry_level))
                else:
                    thrown_items.append((monkey.throw_to_false, worry_level))
                monkey.inspected_items += 1
            monkey.items = []

    monkey_bussines = sorted([monkey.inspected_items for monkey in monkeys])
    return monkey_bussines[-1] * monkey_bussines[-2]


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
