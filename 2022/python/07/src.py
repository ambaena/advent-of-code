from typing import Dict, List
import re


FILES_REGEX = re.compile("^[0-9]+")


def _get_path(path: List) -> str:
    return path[0] + '/'.join(path[1:])


def _add_to_path(path: str, item: str) -> str:
    return path + ('/' if path != '/' else '') + item


def _get_tree(history: List) -> Dict:
    tree = {}
    dir = []
    for line in history:
        if line.startswith('$ cd ..'):
            dir.pop()
        elif line.startswith('$ cd '):
            dir.append(line.split(' ')[-1])
        elif line.startswith('dir '):
            tree[_get_path(dir)] = tree.setdefault(_get_path(dir), []) + [_add_to_path(_get_path(dir), line.split(' ')[-1])]
        elif FILES_REGEX.match(line):
            tree[_get_path(dir)] = tree.setdefault(_get_path(dir), []) + [line]

    for key in tree.keys():
        while any([item.startswith('/') for item in tree[key]]):
            for item in tree[key]:
                if item.startswith('/'):
                    tree[key].remove(item)
                    tree[key] += tree[item]
    return tree


def _get_files_size(files: List) -> int:
    return sum([int(file.split(' ')[0]) for file in files])


def solution_one(input: str) -> int:
    input = input.split('\n')
    return sum([_get_files_size(value) for value in _get_tree(input).values() if _get_files_size(value) < 100000])


def solution_two(input: str) -> int:
    input = input.split('\n')
    disk_needed = 30000000 - (70000000 - _get_files_size(_get_tree(input)['/']))
    return sorted([_get_files_size(value) for value in _get_tree(input).values() if _get_files_size(value) >= disk_needed])[0]


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
