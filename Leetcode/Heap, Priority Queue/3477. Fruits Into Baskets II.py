import heapq

class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        indices = [i for i in range(n)]
        heapq.heapify(indices)
        for i in range(n):
            temp = []
            while indices:
                j = heapq.heappop(indices)
                if fruits[i] <= baskets[j]:
                    while temp:
                        heapq.heappush(indices, temp.pop())
                    break
                else:
                    temp.append(j)
            while temp:
                heapq.heappush(indices, temp.pop())
        return len(indices)