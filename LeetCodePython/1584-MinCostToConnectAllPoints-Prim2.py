#  https://leetcode.com/problems/min-cost-to-connect-all-points/description/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # solution: Minimum Spanning Tree - Prim's Algorithm

        # --- build distance graph
        adj = {i: [] for i in range(len(points))} # (dist, node)
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j))

        # --- init
        visited = set()
        mst = []
        min_cost = 0
        minHeap = [(0,0)] # (cost, node)

        # --- run minimum spanning tree - Prim's
        while len(visited) < len(points):
            cost, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)
            min_cost += cost

            for dist, neighbor in adj[node]:
                heapq.heappush(minHeap, (dist, neighbor))

        # ---
        return min_cost

