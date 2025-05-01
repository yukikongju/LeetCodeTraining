
from typing import List

def is_safe(node, graph, visited) -> bool:
    if visited[node] == 1:
        return True
    if visited[node] == -1: # cycle detected
        return False

    visited[node] = -1
    for neighbor in graph[node]:
        if not is_safe(neighbor, graph, visited):
            return False
    visited[node] = 1

    return True


def get_safe_nodes(graph) -> List[int]:
    v = len(graph)
    visited = [0] * v
    res = []
    for i in range(v):
        if is_safe(i, graph, visited):
            res.append(i)

    return res


if __name__ == "__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(get_safe_nodes(graph))
