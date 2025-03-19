class Solution: # Sliding window. O(n)
    def minOperations(self, nums: list[int]) -> int:
        cnt = 0
        for i in range(2, len(nums)):
            if nums[i-2] == 0:
                cnt += 1
                nums[i-2] ^= 1
                nums[i-1] ^= 1
                nums[i] ^= 1
        if sum(nums) == len(nums):
            return cnt
        else:
            return -1

class Solution: # Brute force. O(n^2)
    def minOperations(self, nums: list[int]) -> int:
        cnt = 0
        def is_possible(i: int) -> bool:
            nonlocal cnt
            if len(nums) - i < 3:
                s = 0
                for j in range(i, len(nums)):
                    s += nums[j]
                num_remaining = len(nums) - i
                return s == num_remaining
            if nums[i] == 0:
                cnt += 1
                for j in range(i, min(len(nums), i+3)):
                    nums[j] ^= 1
                return is_possible(i+1)
            else:
                return is_possible(i+1)
        if is_possible(0):
            return cnt
        else:
            return -1