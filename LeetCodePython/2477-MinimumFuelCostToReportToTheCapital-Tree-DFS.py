#  https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # solution: Preorder Traversal // DFS

        # --- Create Tree from Bidirectional Road matrix
        neighbors = defaultdict(list)
        for x, y in roads:
            neighbors[x].append(y)
            neighbors[y].append(x)

        # --- For each path, find its depth. The number of cars needed will be ceiling(depth // seats)
        cost = 0
        def dfs(node, parent):
            nonlocal cost
            people = 1
            for neighbor in neighbors[node]:
                if neighbor != parent:
                    people += dfs(neighbor, node)
            if node != 0:
                cost += math.ceil(people / seats)

            return people

        # ---
        dfs(0, None)
        return cost

