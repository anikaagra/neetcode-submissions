from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[b].append(a)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not adj_list[course] or adj_list[course] == []:
                return True

            visited.add(course)
            for a in adj_list[course]:
                if dfs(a) == False:
                    return False
            
            visited.remove(course)
            adj_list[course] = []
            return True

        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True