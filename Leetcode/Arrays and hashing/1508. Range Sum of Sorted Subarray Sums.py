class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        newarr = []
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                newarr.append(s)
        newarr.sort()
        
        ans = 0
        for i in range(left-1, right):
            ans += newarr[i]
        return ans%(10**9 + 7)