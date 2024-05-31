from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {}
        for target, prereq in prerequisites:
            if target not in hashmap:
                hashmap[target] = set([prereq])
            else:
                hashmap[target].add(prereq)
        endpoints = set()
        ans = []
        def dfs(course: int, vis: set):
            if course in endpoints:
                return True
            
            if course in vis:
                return False
            else:
                vis.add(course)

            if course in hashmap:
                for p in hashmap[course]:
                    if not dfs(p, vis):
                        return False
                hashmap.pop(course)
            ans.append(course)
            endpoints.add(course)
            return True
        
        for course, p in prerequisites:
            if not dfs(course, set()):
                return []
        
        for course in range(numCourses):
            if course not in endpoints:
                ans.append(course)
        return ans