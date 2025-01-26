from collections import deque

class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        for node in favorite:
            indegree[node] += 1
        
        dq = deque()
        for node in range(n):
            if indegree[node] == 0:
                dq.append(node)
        
        chains = [0] * n
        while dq:
            node = dq.popleft()
            nextnode = favorite[node]
            chains[nextnode] = max(chains[nextnode], chains[node] + 1)
            indegree[nextnode] -= 1
            if indegree[nextnode] == 0:
                dq.append(nextnode)

        visited = [False] * n
        maxcyclesize = 0
        twocycles = 0
        for i in range(n):
            if not visited[i] and indegree[i] > 0:
                cyclesize = 0
                node = i
                while not visited[node]:
                    visited[node] = True
                    node = favorite[node]
                    cyclesize += 1

                if cyclesize == 2:
                    node_a, node_b = i, favorite[i]
                    twocycles += 2 + chains[node_a] + chains[node_b]
                else:
                    maxcyclesize = max(maxcyclesize, cyclesize)
        return max(maxcyclesize, twocycles)