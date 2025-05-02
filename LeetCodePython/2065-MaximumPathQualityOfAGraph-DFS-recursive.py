#  https://leetcode.com/problems/maximum-path-quality-of-a-graph/

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # solution: DFS

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dfs(node, visited, val, cost):
            if node == 0: 
                self.ans = max(self.ans, val)
            for neighbor, weight in graph[node]:
                if cost - weight >= 0:
                    dfs(neighbor, visited | set([neighbor]), val + (neighbor not in visited) * values[neighbor], cost - weight)

        
        self.ans = 0
        dfs(0, set([0]), values[0], maxTime)
        return self.ans

        
