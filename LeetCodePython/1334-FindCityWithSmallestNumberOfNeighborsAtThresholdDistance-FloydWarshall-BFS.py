#  https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # solution: Floyd-Warshall Shortest Path /// BFS

        # --- Build neighbors dictionnary
        neighbors = {i: [] for i in range(n)}
        for u, v, weight in edges:
            neighbors[u].append((v, weight))
            neighbors[v].append((u, weight))

        # --- BFS - Find number of reachable cities for SINGLE city
        def bfs(city):
            city_reached = set()
            minHeap = [(0, city)] # (dist, node)
            visited = set()

            while minHeap:
                dist, node = heapq.heappop(minHeap)
                
                city_reached.add(node)
                visited.add(node)

                for neighbor, weight in neighbors[node]:
                    next_distance = dist + weight
                    if neighbor not in visited and next_distance <= distanceThreshold:
                        heapq.heappush(minHeap, (next_distance, neighbor))

            return len(city_reached) -1 # need to remove itself

        # --- Find number of reachable cities for each cities 
        cities = [0 for _ in range(n)]
        min_num_cities, idx_city = float('inf'), 0
        for city in range(n):
            cities[city] = bfs(city)
            if cities[city] <= min_num_cities:
                min_num_cities = cities[city]
                idx_city = max(city, idx_city)
        
        return idx_city
