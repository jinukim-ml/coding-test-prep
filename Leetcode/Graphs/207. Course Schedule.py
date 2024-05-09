from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.hashmap = {}
        for pair in prerequisites:
            self.hashmap[pair[0]] = self.hashmap.get(pair[0], []) + [pair[1]]

        for i in range(numCourses):
            self.vis = set()
            if not self.dfs(i):
                return False
        return True

    def dfs(self, course: int) -> bool:
        if course in self.vis:
            return False
        if course not in self.hashmap:
            return True

        self.vis.add(course)
        for nextcourse in self.hashmap[course]:
            if nextcourse in self.vis:
                return False
            else:
                if not self.dfs(nextcourse):
                    return False
        self.vis.remove(course)
        self.hashmap.pop(course)
        return True