#  https://leetcode.com/problems/all-paths-from-source-to-target/description/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Solution: DFS
        # Note: graph is already neighbors

        solutions = []
        target = len(graph)-1

        # --- 
        def dfs(i, visited: [int]):
            if (i == target) and (visited not in solutions):
                solutions.append(visited)

            #
            for neighbor in graph[i]:
                dfs(neighbor, visited + [neighbor])
            
        
        dfs(0, [0])

        return solutions

        
