import heapq

class Solution:
    def modifiedGraphEdges(self, n: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:
        self.n = n
        graph = [[] for _ in range(n)]

        for a, b, w in edges:
            if w != -1:
                graph[a].append((b, w))
                graph[b].append((a, w))
        
        curr_shortest = self.dijkstra(graph, source, destination)
        if curr_shortest < target:
            return []
        
        if curr_shortest == target:
            for i, (a, b, w) in enumerate(edges):
                if w == -1:
                    edges[i][-1] = target
            return edges
        
        for i, (a, b, w) in enumerate(edges):
            if w != -1:
                continue
            
            edges[i][-1] = 1
            graph[a].append((b, 1))
            graph[b].append((a, 1))

            new_dist = self.dijkstra(graph, source, destination)

            if new_dist <= target:
                edges[i][2] += target - new_dist

                for j in range(i+1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = target
                return edges
        return []
    
    def dijkstra(self, graph, source, destination):
        mindist = [float('inf')] * self.n
        mindist[source] = 0
        h = [(0, source)] # (distance, node)

        while h:
            d, u = heapq.heappop(h)
            
            if d > mindist[u]:
                continue
            
            for v, w in graph[u]:
                if d + w < mindist[v]:
                    mindist[v] = d + w
                    heapq.heappush(h, (mindist[v], v))
        
        return mindist[destination]