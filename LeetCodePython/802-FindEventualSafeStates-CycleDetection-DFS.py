#  https://leetcode.com/problems/find-eventual-safe-states/description/?envType=problem-list-v2&envId=topological-sort

class Solution:
    def isSafe(self, node, graph, visited) -> bool:
        if visited[node] == 1: # node visited and sage
            return True
        elif visited[node] == -1: # cycle detected
            return False
        
        visited[node] = -1
        for neighbor in graph[node]:
            if not self.isSafe(neighbor, graph, visited):
                return False
        visited[node] = 1
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # solution: DFS - cycle detection 

        v = len(graph)
        visited = [False] * v
        res = []
        for i in range(v):
            if self.isSafe(i, graph, visited):
                res.append(i)
        
        return res

        
