class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # solution: Bellman-Ford + counts number of stops
        
        # --- init
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0

        # --- 
        for i in range(k+1):
            prices_tmp = prices.copy()

            for u, v, p in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + p < prices_tmp[v]:
                    prices_tmp[v] = prices[u] + p
            
            prices = prices_tmp
        
        # --- 
        return -1 if prices[dst] == float('inf') else prices[dst]

