import heapq

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]

        for i in range(len(edges)):
            u, v = edges[i][0], edges[i][1]
            g[u].append((v, succProb[i]))
            g[v].append((u, succProb[i]))
        
        h = [(-1.0, start_node)]
        probs = [0] * n
        probs[start_node] = 1.0
        
        while h:
            cost, u = heapq.heappop(h)
            cost = -cost

            if u == end_node:
                return cost
            
            for v, edge_prob in g[u]:
                new_prob = cost * edge_prob
                if new_prob > probs[v]:
                    probs[v] = new_prob
                    heapq.heappush(h, (-new_prob, v))
        return 0