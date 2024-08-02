class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        total = sum(nums)
        diff = len(nums) - total
        
        ans = sum(nums[:diff])
        cnt = ans
        for l in range(len(nums)):
            r = l + diff
            cnt += nums[r%len(nums)] - nums[l]
            ans = min(ans, cnt)
        return ans