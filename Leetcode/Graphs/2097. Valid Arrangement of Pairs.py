from collections import defaultdict, deque

class Solution: # Finding an Eulerian path using Hierholzer's algorithm. O(E)
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        in_degrees = defaultdict(int)
        out_degrees = defaultdict(int)
        for u, v in pairs:
            graph[u].append(v)
            out_degrees[u] += 1
            in_degrees[v] += 1
        start = self.find_start_node(in_degrees, out_degrees)
        path = deque()
        def dfs(u: int) -> None:
            while graph[u]:
                v = graph[u].pop()
                dfs(v)
            path.appendleft(u)

        dfs(start)
        res = []
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            res.append([u,v])
        return res

    def find_start_node(self, in_degrees: dict, out_degrees: dict) -> int:
        start = 1
        for node in out_degrees.keys():
            if out_degrees[node] - in_degrees[node] == 1: # unique starting node
                return node
            
            if out_degrees[node] > 0: # one of the candidates
                start = node
        return start