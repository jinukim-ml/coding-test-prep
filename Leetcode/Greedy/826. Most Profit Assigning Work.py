from typing import List
import heapq

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse=True)

        pairs = []
        for d, p in zip(difficulty, profit):
            heapq.heappush(pairs, (d, p))
        
        pick_profit = []
        ans = 0
        for i in range(len(worker)):
            while pairs and pairs[0][0] <= worker[i]:
                d, p = heapq.heappop(pairs)
                heapq.heappush(pick_profit, (-p, d))
            
            while pick_profit and pick_profit[0][1] > worker[i]:
                heapq.heappop(pick_profit)
            if pick_profit:
                ans -= pick_profit[0][0]
            else:
                return ans
        return ans