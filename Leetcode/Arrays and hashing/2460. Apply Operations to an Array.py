class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        nonzeros = []
        zeros = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i]:
                nonzeros.append(nums[i])
            else:
                zeros.append(nums[i])
        if nums[-1]:
            nonzeros.append(nums[-1])
        else:
            zeros.append(nums[-1])
        return nonzeros + zeros