# https://atcoder.jp/contests/abc305/tasks/abc305_e
# !python3 % < AtCoder/ABC305/inputs/e1.in;

import heapq
from collections import defaultdict

# --- 1. read inputs
N, M, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
guards = [tuple(map(int, input().split())) for _ in range(K)]

# --- 2. Run multisources BFS - dijkstra
maxHeap = [(-h, p) for p, h in guards]
heapq.heapify(maxHeap)
distances = [float('inf') for _ in range(N+1)]

while maxHeap:
    h, p = heapq.heappop(maxHeap)

    if distances[p] == float('inf'):
        distances[p] = h
        if h+1 <= 0:
            for neighbor in graph[p]: heapq.heappush(maxHeap, (h+1, neighbor))
    elif distances[p] > h:
        distances[p] = h
        if h+1 <= 0:
            for neighbor in graph[p]:
                if distances[neighbor] > h+1:
                    heapq.heappush(maxHeap, (h+1, neighbor))

# --- 3. print output
res = []
for vertex, dist in enumerate(distances):
    if dist <= 0:
        res.append(vertex)

print(len(res))
print(*res)
