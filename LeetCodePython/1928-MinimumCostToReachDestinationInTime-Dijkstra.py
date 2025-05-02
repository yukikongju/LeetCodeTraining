#  https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # solution: dijkstra

        # --- build the graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # --- dijkstra
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n = len(passingFees) # num vertices
        distances = [float('inf')] * n
        fees = [float('inf')] * n
        visited = [False] * n

        pq = [(passingFees[0], 0, 0)] # (fee, distance, node)
        distances[0] = 0
        visited[0] = True
        fees[0] = passingFees[0]

        while pq:
            fee, dist, node = heapq.heappop(pq)
            if node == n - 1:
                return fee

            for neighbor, weight in graph[node]:
                if dist + weight > maxTime:
                    continue
                new_dist = dist + weight
                new_fee = fee + passingFees[neighbor]

                if new_fee < fees[neighbor] or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    fees[neighbor] = new_fee
                    heapq.heappush(pq, (new_fee, new_dist, neighbor))

        return -1
   
