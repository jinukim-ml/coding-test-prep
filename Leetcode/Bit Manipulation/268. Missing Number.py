from typing import List

class Solution: # bit manipualtion solution using associative property of XOR
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)+1):
            ans ^= i
        
        for n in nums:
            ans ^= n
        
        return ans

class Solution: # using sum formula
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums))*(len(nums)+1))//2 - sum(nums)