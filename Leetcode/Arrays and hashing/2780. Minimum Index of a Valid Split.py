from collections import Counter, defaultdict

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        counter = Counter(nums)
        curr_cnt = defaultdict(int)
        for i in range(len(nums)-1):
            curr_cnt[nums[i]] += 1
            left_length = i+1
            right_length = len(nums)-i-1
            if curr_cnt[nums[i]] > left_length//2 and counter[nums[i]] - curr_cnt[nums[i]] > right_length//2:
                return i
        return -1