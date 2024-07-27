import heapq

class Solution: # Dijkstra's algorithm
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        def dijkstra(source, adj):
            q = [(source, 0)]
            distances = [-1] * 26

            while q:
                char, d = heapq.heappop(q)
                for ch, dist in adj[char]:
                    if distances[ch] == -1 or d + dist < distances[ch]:
                        distances[ch] = d + dist
                        heapq.heappush(q, (ch, distances[ch]))
            return distances
        
        adj = [[] for _ in range(26)]
        for i in range(len(original)):
            adj[ord(original[i]) - 97].append((ord(changed[i]) - 97, cost[i]))
        
        book = {}
        for ch in range(26):
            distances = dijkstra(ch, adj)
            book[ch] = distances
        
        ans = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                dist = book[ord(source[i]) - 97][ord(target[i]) - 97]
                if dist == -1:
                    return -1
                ans += dist
        return ans

class Solution: # Floyd-Warshall algorithm
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        g = [[float('inf') for __ in range(26)] for _ in range(26)]
        for d in range(26):
            g[d][d] = 0
        
        for i in range(len(original)):
            og, ch = ord(original[i]) - 97, ord(changed[i]) - 97
            g[og][ch] = min(g[og][ch], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        
        ans = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                distance = g[ord(source[i]) - 97][ord(target[i]) - 97]
                if distance == float('inf'):
                    return -1
                ans += distance
        return ans