

'''OldLock finds a way to solve a wheels based lock some wheels of which are broken.
To simplify, it finds a way from one point of the graph to another.
Graph was a fully connected one, but some connections were removed (the lock got rusty)'''

def solve_lock(target: str, deadends: list, lock_length: int) -> list:
    return rolling_wheels(target, lock_length, deadends)


def generate_neighbours(point: str) -> list:
    neighbours = []
    for i in range(len(point)):
        minus_neighbours = list(point)
        plus_neighbours = list(point)
        minus_neighbours[i] = str((int(minus_neighbours[i]) - 1) % 10)
        plus_neighbours[i] = str((int(plus_neighbours[i]) + 1) % 10)
        neighbours.append("".join(plus_neighbours))
        neighbours.append("".join(minus_neighbours))
    return neighbours


def rolling_wheels(target: str, lock_length: int, deadends: list):
    path = []
    visited = {}
    queue = ['0' * lock_length]
    for point in queue:
        if point == target:
            visited['no_need_for_neighbours'] = point
            new_element = point
            while new_element != '0' * lock_length:
                path.append(new_element)
                new_element = visited[new_element]
            path.append('0' * lock_length)
            path.reverse()
            return path
        if point not in visited.values() and point not in deadends:
            for i in generate_neighbours(point):
                if i not in visited:
                    queue.append(i)
                    visited[i] = point
        del point
    return None

