#  https://leetcode.com/problems/number-of-provinces/description/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # solution: dfs

        # --- init: neighbors list 
        n = len(isConnected)
        visited = [False for _ in range(n)]
        num_provinces = 0
        neighbors = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if (isConnected[i][j] == 1) and (i!=j):
                    neighbors[i].append(j)
        
        def dfs(city):
            if not visited[city]:
                visited[city] = True
                for next_city in neighbors[city]:
                    if not visited[next_city]:
                        dfs(next_city)

        # --- count connected component
        for city in range(n):
            if not visited[city]:
                num_provinces += 1
                dfs(city)
        

        # ---
        return num_provinces
                
