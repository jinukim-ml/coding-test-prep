from collections import defaultdict
import heapq

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        freq = defaultdict(list)
        for i, n in enumerate(nums):
            s = 0
            while n > 0:
                s += n%10
                n//= 10
            heapq.heappush(freq[s], -nums[i])
        
        res = -1
        for k, v in freq.items():
            if len(v) >= 2:
                biggest = -heapq.heappop(freq[k])
                second_biggest = -heapq.heappop(freq[k])
                res = max(res, biggest + second_biggest)
        return res