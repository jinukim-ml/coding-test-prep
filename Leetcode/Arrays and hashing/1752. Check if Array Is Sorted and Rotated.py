class Solution:
    def check(self, nums: list[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                cnt += 1
        if cnt > 1:
            return False
        elif cnt == 1:
            return nums[0] >= nums[-1]
        else:
            return True