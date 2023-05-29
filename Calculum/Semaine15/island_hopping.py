# 
#  https://open.kattis.com/problems/islandhopping
# !python % < ~/Projects/LeetCodeTraining/Calculum/Semaine15/island_hopping/1.in

#  SyntaxError: unexpected EOF while parsing

# Solution:
# (1) create graph: O(n log n)
# (2) Prim's

import math
import heapq


def read_input():
    n = int(input())
    problems = []
    for _ in range(n):
        m = int(input())
        print(m)
        bridges = []
        for _ in range(m):
            bridges.append(list(map(float, input().split())))
        problems.append(bridges)
    return problems

def read_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        problems = []
        for _ in range(n):
            m = int(file.readline().strip())
            bridges = []
            for _ in range(m):
                bridges.append(list(map(float, file.readline().split())))
            problems.append(bridges)
    return problems

def solve(problems):
    for problem in problems:
        ans = _solve(problem)
        print(ans)

def _solve(problem):
    graph = create_graph(problem)
    spanning_tree = prim(graph)
    return calculate_total_bridge_length(spanning_tree)
     

def calculate_total_bridge_length(spanning_tree):
    """ 
    spanning_tree = [(source, target, dist)]
    """
    total = 0
    for source, target, dist in spanning_tree:
        total += dist
    return total


def create_graph(problem):
    """ 
    given list of island positions (x,y), return graph of distance between 
    each island
    """
    n = len(problem)
    graph = {i: [] for i in range(n)}
    for i, (x1, y1) in enumerate(problem):
        for j, (x2, y2) in enumerate(problem[i+1:]):
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            graph[i].append((i+1+j, dist))
            graph[i+1+j].append((i, dist))
    return graph

def prim(graph):
    start_node = next(iter(graph))

    # init data struct
    visited = set([start_node])
    min_heap = []
    min_spanning_tree = []

    # add edges of starting nodes to min heap
    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    # prim algo's
    while min_heap:
        weight, source, target = heapq.heappop(min_heap)

        if target in visited:
            continue

        min_spanning_tree.append((source, target, weight))
        visited.add(target)

        # add edges of target node to min heap
        for neighbor, weight in graph[target]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, target, neighbor))

    return min_spanning_tree


def main():
    #  problems = read_input()
    problems = read_file('Calculum/Semaine15/island_hopping/1.in')
    #  print(problems)
    solve(problems)

if __name__ == "__main__":
    main()

