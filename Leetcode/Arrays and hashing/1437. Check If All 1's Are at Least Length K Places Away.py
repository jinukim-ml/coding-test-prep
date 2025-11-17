class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        prev = -k-1
        for i, n in enumerate(nums):
            if n == 1:
                if i-prev-1 < k:
                    return False
                prev = i
        return True