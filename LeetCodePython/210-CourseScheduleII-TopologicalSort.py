#  https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Solution: Topological Sort - DFS

        def dfs(i, seen):
            if seen[i] == -1: # re-visiting a course, so this is a cycle
                return False
            if seen[i] == 1: 
                return True

            # DFS through course
            seen[i] = -1 
            for u in adj[i]:
                if not dfs(u, seen):
                    return False
            res.append(i)
            seen[i] = 1
            return True

        ## build prereq_list
        adj = [[] for i in range(numCourses)]
        for (succ, prev) in prerequisites:
            adj[prev].append(succ)
        
        ## 
        seen = [0 for _ in range(numCourses)]
        res = []
        for i in range(numCourses):
            if not dfs(i, seen):
                return [] # cycle found
        
        return res[::-1]
