class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        book = {k: v for v, k in enumerate(nums)}
        ans = -1
        streaks = {}

        for i, n in enumerate(nums):
            curr = 1
            squared = n**2
            if squared in book:
                if squared in streaks:
                    curr += streaks[squared]
                else:
                    while squared in book:
                        squared = squared**2
                        curr += 1
                streaks[n] = curr
                ans = max(ans, curr)
        return ans