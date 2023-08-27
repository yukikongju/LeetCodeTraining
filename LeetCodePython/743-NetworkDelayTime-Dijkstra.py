class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Solution: Dikjstra - Shortest Path: BFS + MinHeap
        # HEAP: (value, node) --- sort using first value

        # --- init
        edges = [[] for _ in range(n+1)]
        distances = [float('inf') for _ in range(n+1)]
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            distances[node] = dist

            for neighbor, weight in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (dist+weight, neighbor))
        

        return max(distances[1:]) if len(visited) == n else -1

