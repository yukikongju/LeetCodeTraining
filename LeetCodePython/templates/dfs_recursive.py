def dfs(graph, visited, node):
    if node in visited:
        return 
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor)
