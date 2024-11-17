class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        arr = []
        for i in range(len(nums)):
            right_sum -= nums[i]
            arr.append((left_sum, right_sum))
            left_sum += nums[i]

        ans = 0
        for i, (l, r) in enumerate(arr):
            if nums[i] == 0:
                if r == l:
                    ans += 2
                elif r == l + 1:
                    ans += 1
                elif l == r + 1:
                    ans += 1
        return ans