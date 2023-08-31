#  https://leetcode.com/problems/path-with-maximum-probability/description/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # solution: Dijkstra

        # --- construct neighbors
        neighbors = {node: [] for node in range(n)} # neighbors[u] = (v, proba)
        for i, (u, v) in enumerate(edges):
            proba = succProb[i]
            neighbors[u].append((v, proba))
            neighbors[v].append((u, proba))

        # --- Dijkstra - BFS + maxHeap
        distances = [0 for _ in range(n)]
        distances[start_node] = 1
        maxHeap = [(-1, start_node)]

        while maxHeap:
            proba, node = heapq.heappop(maxHeap)
            proba *= -1
            
            if node == end_node:
                return proba
            
            for neighbor, weight in neighbors[node]:
                next_proba = proba * weight
                if next_proba > distances[neighbor]:
                    distances[neighbor] = next_proba
                    heapq.heappush(maxHeap, (-next_proba, neighbor))

        return 0 
