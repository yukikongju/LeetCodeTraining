#  https://leetcode.com/problems/course-schedule/description/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # solution: dfs

        # --- prerequisites maps
        prereqs_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs_map[course].append(prereq)

        # --- 
        visited = set()

        def dfs(course: int):
            # check for loop in graph
            if course in visited: 
                return False
            
            # if no prerequisites
            if prereqs_map[course] == []:
                return True
            
            # check if we can reach prerequisites
            visited.add(course)
            for prereq in prereqs_map[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            prereqs_map[course] = [] # avoid performing dfs again if we run into same case
            return True
            

        # --- run dfs to see if we can reach each course
        for course in range(numCourses):
            if not dfs(course): 
                return False
        
        return True



        
