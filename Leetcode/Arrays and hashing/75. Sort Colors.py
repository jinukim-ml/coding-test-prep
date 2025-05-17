from collections import Counter

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        counter = Counter(nums)
        i = 0
        for v in range(3):
            for _ in range(counter[v]):
                nums[i] = v
                i += 1