MOVEMENT = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}


def _are_touching(hail: tuple, tail: tuple) -> bool:
    return (abs(hail[0] - tail[0]) <= 1 and abs(hail[1] - tail[1]) <= 1)


def _move(direction: str, knot: tuple) -> tuple:
    return (knot[0] + MOVEMENT[direction][0], knot[1] + MOVEMENT[direction][1])


def _move_tail(head: tuple, tail: tuple) -> tuple:
    if head == tail or _are_touching(head, tail):
        return tail
    elif head[0] == tail[0]:
        move = 'U' if head[1] > tail[1] else 'D'
        return _move(move, tail)
    elif head[1] == tail[1]:
        move = 'R' if head[0] > tail[0] else 'L'
        return _move(move, tail)
    else:
        move_one = 'U' if head[1] > tail[1] else 'D'
        move_two = 'R' if head[0] > tail[0] else 'L'
        tail = _move(move_one, tail)
        return _move(move_two, tail)


def solution_one(input: str) -> int:
    rules = [(movement.split(' ')[0], int(movement.split(' ')[1])) for movement in input.split('\n')]
    head, tail = (0, 0), (0, 0)
    visited_by_tail = []
    for direction, moves in rules:
        for _ in range(moves):
            head = _move(direction, head)
            tail = _move_tail(head, tail)
            visited_by_tail.append(tail)
    return len(set(visited_by_tail))


def solution_two(input: str) -> int:
    rules = [(movement.split(' ')[0], int(movement.split(' ')[1])) for movement in input.split('\n')]
    knots = [(0, 0) for _ in range(10)]
    visited_by_tail = []
    for direction, moves in rules:
        for _ in range(moves):
            for knot_idx in range(len(knots)):
                if knot_idx == 0:
                    knots[knot_idx] = _move(direction, knots[knot_idx])
                else:
                    knots[knot_idx] = _move_tail(knots[knot_idx-1], knots[knot_idx])
            visited_by_tail.append(knots[-1])
    return len(set(visited_by_tail))


if __name__ == "__main__":
    input = open('input').read()
    print(f"Solution 1: {solution_one(input)}")
    print(f"Solution 2: {solution_two(input)}")
