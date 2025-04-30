from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        # PROCESS NODE

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)


