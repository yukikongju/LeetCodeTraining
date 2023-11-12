# !python3 % < CSES/GraphAlgorithms/inputs/MessageRoute.in;

from collections import defaultdict

# read graph
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# run bfs to find if we can reach
visited = set() # node
visited.add(1)
q = [(1, 0)]
distances = defaultdict(int)
#  distances[1] = 0
while q:
    node, dist = q.pop(0)

    if node == n:
        min_path = dist+1
        # finding a path
        path = [node]
        curr = node
        while True:
            path.append(distances[curr])
            curr = distances[curr]
            if curr == 1: break
        path = path[::-1]
        print(len(path))
        print(*path)
        exit(0)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            q.append((neighbor, dist+1))
            visited.add(neighbor)
            distances[neighbor] = node

# find path

print("IMPOSSIBLE")


