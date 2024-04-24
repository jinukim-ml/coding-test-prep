from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        nswer = []
        for i in range(len(nums)):
            pivot = i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = pivot+1, len(nums)-1

            
            while left < right:
                sum3 = nums[pivot] + nums[left] + nums[right]
                if sum3 > 0:
                    right -= 1
                elif sum3 < 0:
                    left += 1
                else:
                    nswer.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return nswer