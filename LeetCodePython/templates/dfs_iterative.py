def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        # processing

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

