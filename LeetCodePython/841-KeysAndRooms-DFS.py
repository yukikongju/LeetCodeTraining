#  https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # solution: dfs
        visited = [False for _ in range(len(rooms))]
        visited[0] = True
        stack = rooms[0]

        # ---
        while stack:
            next_room = stack.pop(0)
            if not visited[next_room]:
                for key in rooms[next_room]:
                    stack.append(key)
                visited[next_room] = True

        # --- check if all rooms have been visited
        for v in visited:
            if v == False:
                return False
        return True
