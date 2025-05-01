# https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
# kahn's algorithm for topological sort - uses BFS and in-degrees
# note: topological sort only works for DAGs, so we need to check for cycle

from collections import defaultdict, deque
from typing import List

def topological_sort(num_nodes, edges) -> List[int]:
    # build the adjacency graph + compute in-degrees
    graph = defaultdict(list)
    indegrees = [0] * num_nodes
    for u, v in edges:
        graph[u].append(v)
        indegrees[v] += 1

    # queue starting vertices with in degrees of 0 
    queue = deque([i for i in range(num_nodes) if indegrees[i] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    # check cycle
    return result if len(result) == num_nodes else []

if __name__ == "__main__":
    V = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    result = topological_sort(V, edges)
    if result:
        print("Topological Order:", result)

