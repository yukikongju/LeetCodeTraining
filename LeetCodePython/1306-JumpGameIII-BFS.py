class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # solution: BFS => 

        # --- visit all positions from start with BFS
        q = deque([start])
        visited = set() 
        
        while q:
            idx = q.popleft()

            if idx in visited:
                continue
            
            # visit neighbor 
            if idx + arr[idx] < len(arr):
                q.append(idx + arr[idx])
            if idx - arr[idx] >= 0:
                q.append(idx - arr[idx])
            
            #
            visited.add(idx)

        # --- check if all zeros positions have been visited
        zero_positions = [i for i, n in enumerate(arr) if n == 0]
        return any([True if i in visited else False for i in zero_positions])

