from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        g = defaultdict(list)
        for u, v in prerequisites:
            g[u].append(v)

        visited = set()
        prereq_map = defaultdict(set)
        def dfs(node: int, visited: set) -> None:
            if node in visited:
                return
            visited.add(node)
            for v in g[node]:
                prereq_map[node].add(v)
                dfs(v, visited)
                for course in prereq_map[v]:
                    prereq_map[node].add(course)

        for i in range(numCourses):
            dfs(i, visited)
        res = []
        for u, v in queries:
            if v in prereq_map[u]:
                res.append(True)
            else:
                res.append(False)
        return res