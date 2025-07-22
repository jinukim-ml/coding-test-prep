class Solution: # dictionary solution
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        indices = {}
        l, curr, res = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] in indices:
                target = indices[nums[r]]
                while l <= target:
                    curr -= nums[l]
                    l += 1
            indices[nums[r]] = r
            curr += nums[r]
            res = max(res, curr)
        return res

class Solution: # set solution
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        stored = set()
        l, curr, res = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] in stored:
                while nums[l] != nums[r]:
                    curr -= nums[l]
                    stored.remove(nums[l])
                    l += 1
                l += 1
            else:
                curr += nums[r]
                stored.add(nums[r])
                res = max(res, curr)
        return res