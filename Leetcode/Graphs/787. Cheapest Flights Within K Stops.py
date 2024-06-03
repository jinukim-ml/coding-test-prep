from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices[:]
            for s, d, p in flights: # source, destination, price
                if prices[s] == float('inf'):
                    continue

                if p + prices[s] < temp[d]:
                    temp[d] = p + prices[s]
            prices = temp
        
        return -1 if prices[dst] == float('inf') else prices[dst]