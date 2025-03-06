# Inspired by this beautiful solution by Alexander Voitenko on Leetcode (https://leetcode.com/problems/find-missing-and-repeated-values/solutions/4763547/fast-o-1-memory-solution-with-math-explained/)
class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        expected_sum = (n**2 * (n**2+1))//2
        expected_ssq = (n**2 * (n**2+1) * (2*n**2 + 1))//6
        s, ssq = 0, 0
        for row in grid:
            for num in row:
                s += num
                ssq += num**2
        
        diff = expected_sum - s
        diff_sq = expected_ssq - ssq

        duplicate = (diff_sq - diff**2) // (2*diff)
        removed = diff + duplicate
        return [duplicate, removed]