#  https://leetcode.com/problems/course-schedule-iv/?envType=problem-list-v2&envId=topological-sort

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # solution: topological sort - kahn's algorithm 
        # intuition:
        # 0. Build adjacency graph
        # 1. Topological Sort to establish order
        # 2. 
        # 
        
        # build adjacency graph + in-degrees
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1

        # topological sort
        q = deque()
        for u in range(numCourses):
            if indegrees[u] == 0:
                q.append(u)

        mapping = defaultdict(set)
        while q:
            node = q.popleft()
            for next_course in graph[node]:
                mapping[next_course].add(node)
                mapping[next_course].update(mapping[node])
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    q.append(next_course)
        
        return [prereq in mapping[course] for prereq, course in queries]


        

