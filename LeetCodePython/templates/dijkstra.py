# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

import heapq
from collections import defaultdict


def dijkstra(V, edges, src):
    # build the adjacency graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append([v, w])
        graph[v].append([u, w])

    # compute distances
    pq = []
    distances = [float('inf')] * V
    distances[src] = 0
    heapq.heappush(pq, [0, src])

    while pq:
        _, u = heapq.heappop(pq)

        for v, w in graph[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                heapq.heappush(pq, [distances[v], v])

    return distances


if __name__ == "__main__":
    V = 5
    src = 0

    # edge list format: {u, v, weight}
    edges =[[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]];

    result = dijkstra(V, edges, src)
    print(result)
