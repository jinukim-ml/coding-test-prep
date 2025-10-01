class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))]
        max_len, max_cnt = 0, 0
        for i in range(len(nums)-1, -1, -1):
            lis_len, lis_cnt = 1, 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    if dp[j][0]+1 > lis_len:
                        lis_len = dp[j][0] + 1
                        lis_cnt = dp[j][1]
                    elif dp[j][0]+1 == lis_len:
                        lis_cnt += dp[j][1]
            dp[i] = [lis_len, lis_cnt]
            if lis_len > max_len:
                max_len = lis_len
                max_cnt = lis_cnt
            elif lis_len == max_len:
                max_cnt += lis_cnt
        return max_cnt