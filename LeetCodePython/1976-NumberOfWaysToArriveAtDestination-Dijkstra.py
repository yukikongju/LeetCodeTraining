#  https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/?envType=problem-list-v2&envId=topological-sort

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # solution: dijkstra + dp 
        # DP: number of ways to reach node X

        # - build the graph
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # - dijkstra
        distances = [float('inf')] * n
        dp = [0] * n

        distances[0] = 0
        dp[0] = 1
        pq = [(0, 0)] # (distance, node)

        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            
            for neighbor, weight in graph[node]:
                if dist + weight < distances[neighbor]:
                    distances[neighbor] = dist + weight
                    dp[neighbor] = dp[node]
                    heapq.heappush(pq, (distances[neighbor], neighbor))
                elif dist + weight == distances[neighbor]:
                    dp[neighbor] = (dp[neighbor] + dp[node]) % MOD

        return dp[-1]

