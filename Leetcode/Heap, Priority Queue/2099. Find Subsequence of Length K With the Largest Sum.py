import heapq

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        h = []
        total = 0
        for i, n in enumerate(nums):
            if len(h) < k:
                heapq.heappush(h, (n, i))
                total += n
            else:
                if n > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (n,i))
        
        temp = []
        while h:
            n, i = heapq.heappop(h)
            heapq.heappush(temp, (i,n))
        res = []
        while temp:
            _, n = heapq.heappop(temp)
            res.append(n)
        return res

class Solution: # shorter solution
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        for i, n in enumerate(nums):
            nums[i] = (n,i)
        nums.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(nums[i])
        res.sort(key=lambda x: x[1])
        for i in range(k):
            res[i] = res[i][0]
        return res