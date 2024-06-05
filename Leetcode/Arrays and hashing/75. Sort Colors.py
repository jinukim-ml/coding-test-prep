from typing import List
from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        table = defaultdict(int)
        for n in nums:
            table[n] += 1
        
        for i in range(table[0]):
            nums[i] = 0
        for i in range(table[0], table[0] + table[1]):
            nums[i] = 1
        for i in range(table[0]+table[1], len(nums)):
            nums[i] = 2