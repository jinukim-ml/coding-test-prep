class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums)):
            while stack and stack[-1] >= nums[i]:
                if stack[-1] > nums[i]:
                    res += 1
                stack.pop()
            if nums[i]:
                stack.append(nums[i])
        return res + len(stack)