class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        window_sum = 0
        table = {}
        unique = set()
        ans = 0
        
        for r in range(len(nums)):
            window_sum += nums[r]
            unique.add(nums[r])
            table[nums[r]] = table.get(nums[r], 0) + 1

            if len(unique) == k:
                ans = max(ans, window_sum)
            
            if r >= k-1:
                l = r - k + 1
                window_sum -= nums[l]
                if table[nums[l]] == 1:
                    unique.remove(nums[l])
                table[nums[l]] -= 1
        return ans