from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = 1
        prefix_products = [1]

        suffix = 1
        suffix_products = [1]
        for i in range(len(nums)-1):
            prefix *= nums[i]
            prefix_products.append(prefix)
        
            suffix *= nums[n-(i+1)]
            suffix_products.append(suffix)

        answer = []
        for i in range(n):
            answer.append(prefix_products[i] * suffix_products[n-(i+1)])
        return answer