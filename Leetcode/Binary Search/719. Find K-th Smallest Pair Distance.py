class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            cnt, l = 0, 0

            for r in range(len(nums)):
                while nums[r] - nums[l] > mid:
                    l += 1
                cnt += r - l
            
            if cnt >= k:
                high = mid
            else:
                low = mid + 1
        return low