class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        maximum = max(nums)

        primes = [1] * (maximum + 1)
        primes[1] = 0
        for i in range(2, int((maximum + 1)**0.5) + 1):
            if primes[i] == 1:
                for j in range(i * i, maximum + 1, i):
                    primes[j] = 0

        curr = 1
        i = 0
        while i < len(nums):
            diff = nums[i] - curr
            if diff < 0:
                return False

            if primes[diff] or diff == 0:
                i += 1
                curr += 1
            else:
                curr += 1
        return True