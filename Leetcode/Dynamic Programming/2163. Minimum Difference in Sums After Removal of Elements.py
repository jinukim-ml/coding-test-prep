import heapq

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        length = len(nums)
        n = length//3
        
        prefix, suffix = [0 for _ in range(length)], [0 for _ in range(length)]
        maxheap, minheap = [], []
        maxheap_sum = 0
        for i in range(length):
            maxheap_sum += nums[i]
            heapq.heappush(maxheap, -nums[i])

            if len(maxheap) > n:
                popped = heapq.heappop(maxheap)
                maxheap_sum += popped
            if len(maxheap) == n:
                prefix[i] = maxheap_sum
        
        minheap_sum = 0
        for i in range(length-1, -1, -1):
            minheap_sum += nums[i]
            heapq.heappush(minheap, nums[i])

            if len(minheap) > n:
                popped = heapq.heappop(minheap)
                minheap_sum -= popped
            if len(minheap) == n:
                suffix[i] = minheap_sum
        
        res = float('inf')
        for i in range(n-1, 2*n):
            res = min(res, prefix[i] - suffix[i+1])
        return res