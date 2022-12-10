from typing import List


def _is_visible(tree_line: List, idx: int) -> bool:
    one_side = all([(tree_line[idx] > tree) for tree in tree_line[: idx]])
    other_side = all([(tree_line[idx] > tree) for tree in tree_line[idx+1:]])
    return any([one_side, other_side])


def _get_scenic_score(tree_line: List, idx: int) -> int:
    score_one = 0
    for tree in tree_line[: idx][-1::-1]:
        score_one += 1
        if tree >= tree_line[idx]:
            break

    score_two = 0
    for tree in tree_line[idx+1:]:
        score_two += 1
        if tree >= tree_line[idx]:
            break

    return score_one * score_two


def solution_one(input: str) -> int:
    forest = [[*tree] for tree in input.split('\n')]
    rows, cols = range(len(forest)), range(len(forest[0]))
    count = 0
    for row_idx in rows:
        for col_idx in cols:
            is_visible_x = _is_visible(forest[row_idx], col_idx)
            is_visible_y = _is_visible([forest[_][col_idx] for _ in rows], row_idx)
            if any([is_visible_x, is_visible_y]):
                count += 1
    return count


def solution_two(input: str) -> int:
    forest = [[*tree] for tree in input.split('\n')]
    rows, cols = range(len(forest)), range(len(forest[0]))
    scenic_score = 0
    for row_idx in rows:
        for col_idx in cols:
            scenic_score_x = _get_scenic_score(forest[row_idx], col_idx)
            scenic_score_y = _get_scenic_score([forest[_][col_idx] for _ in rows], row_idx)
            scenic_score = max([scenic_score, scenic_score_x * scenic_score_y])
    return scenic_score


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
