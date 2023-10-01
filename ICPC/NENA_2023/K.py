# !python3 % < ICPC/NENA_2023/inputs/K1.in;
# !python3 % < ICPC/NENA_2023/inputs/K2.in;
# !python3 % < ICPC/NENA_2023/inputs/K3.in;

from collections import defaultdict
import heapq


# --- 1. read inputs + create graph
n, m = map(int, input().split(' '))
graph = defaultdict(list)
edges = []
for _ in range(m):
    a, b, w = map(int, input().split(' '))
    graph[a].append((b, w))
    graph[b].append((a, w))
    edges.append((a,b,w))


# --- 2. Run Prim's algorithm to find mst with maxheap
def prim(graph):
    start_vertex = 1
    mst = []
    mst_weight = 0
    visited = set()
    min_heap = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapq.heapify(min_heap)

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        visited.add(u)

        if v not in visited:
            mst.append((u, v, weight))
            mst_weight += weight

            for neighbor, edge in graph[v]:
                heapq.heappush(min_heap, (edge, v, neighbor))

    return mst_weight


# --- 3. Run MST on all subgraphs (remove one edge) -> MST: O(E + V log V) * E graphs

max_value = 0
for a, b, w in edges:
    # temporarily remove edge
    graph[a].remove((b, w))
    graph[b].remove((a, w))

    res = prim(graph)
    max_value = max(max_value, res)

    # add edge back
    graph[a].append((b, w))
    graph[b].append((a, w))

print(max_value)

