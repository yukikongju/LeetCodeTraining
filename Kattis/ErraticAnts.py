#  https://open.kattis.com/problems/erraticants
#  !python3 % < Kattis/inputs/erratic_ants1.in;

from collections import defaultdict


# --- 1. read inputs
N = int(input())

directions = {'S': (1, 0), 'N': (-1, 0), 'E': (0, 1), 'W': (0, -1)}

def bfs(graph, start, end):
    queue = [(start, 0)] # ( (x, y), dist )
    visited = set()
    while queue:
        node, dist = queue.pop(0)
        visited.add(node)

        if node == end: return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist+1))

# --- 2. 
sols = []
for _ in range(N):
    input()
    M = int(input())
    A = [input() for _ in range(M)]

    # - build graph
    x, y = 0, 0
    start = current = tuple((x, y))
    graph = defaultdict(list)
    for a in A:
        dx, dy = directions[a]
        x, y = x+dx, y+dy
        _next = tuple((x, y))
        graph[current].append(_next)
        graph[_next].append(current)
        current = _next
    end = current

    # - run bfs on graph
    dist = bfs(graph, start, end)
    sols.append(dist)


# --- 3. 
for sol in sols: print(sol)


