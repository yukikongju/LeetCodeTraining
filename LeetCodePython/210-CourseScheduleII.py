#  https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # solution: topological sort -> reverse dfs

        # --- create prerequisites mapping
        prereq_maps = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_maps[course].append(prereq)
        
        # --- dfs with cycle detection: visiting vs visited
        visited, cycle = set(), set()
        results = []
        
        def has_cycle(course: int):
            if course in cycle:
                return True
            if course in visited:
                return False
            
            cycle.add(course)
            for prereq in prereq_maps[course]:
                if has_cycle(prereq):
                    return True
            cycle.remove(course)
            visited.add(course)
            results.append(course)

            return False

        # --- 
        for course in range(numCourses):
            if has_cycle(course):
                return []
        
        return results
