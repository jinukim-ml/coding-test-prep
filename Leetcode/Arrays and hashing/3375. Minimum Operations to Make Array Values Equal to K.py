class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        seen = set()
        for n in nums:
            if n < k:
                return -1
            seen.add(n)
        if k in seen:
            return len(seen) - 1
        else:
            return len(seen)