from collections import defaultdict

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        merged = []
        for i in range(len(nums)):
            for n in nums[i]:
                merged.append((n, i))

        merged.sort()
        freq = defaultdict(int)
        l, cnt = 0, 0
        start, end = 0, float('inf')

        for r in range(len(merged)):
            freq[merged[r][1]] += 1
            if freq[merged[r][1]] == 1:
                cnt += 1
            
            while cnt == len(nums):
                curr = merged[r][0] - merged[l][0]
                if curr < end - start:
                    start = merged[l][0]
                    end = merged[r][0]
                
                freq[merged[l][1]] -= 1
                if freq[merged[l][1]] == 0:
                    cnt -= 1
                l += 1
        return [start, end]