class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        indices = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for i, n in enumerate(nums2):
            while stack and n > stack[-1]:
                val = stack.pop()
                res[indices[val]] = n
            if n in indices:
                stack.append(n)
        return res