
#  https://leetcode.com/problems/reconstruct-itinerary/description/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # solution: Eulerian Paths - DFS
        # explanation: https://leetcode.com/problems/reconstruct-itinerary/solutions/709590/python-short-euler-path-finding-o-e-log-e-explained/

        # ---
        def dfs(airport):
            while adj[airport]:
                candidate = adj[airport].pop(0)
                dfs(candidate)
            route.append(airport)

        # --- init: create adjancy list and sort elements
        route = []
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        for key in adj:
            adj[key] = sorted(adj[key], reverse=False)
        
        # --- find eulerian path
        dfs("JFK")
        return route[::-1]



        
