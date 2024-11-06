class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        i = 0
        arrs = []
        while i < len(nums):
            curr = [nums[i]]
            ones = bin(nums[i]).count('1')
            j = i+1
            while j < len(nums) and ones == bin(nums[j])[2:].count('1'):
                curr.append(nums[j])
                j += 1
            i = j
            arrs.append(sorted(curr))
        
        for i in range(1, len(arrs)):
            if arrs[i-1][-1] > arrs[i][0]:
                return False
        return True