class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        counts = [0,0]
        book = {}
        res = 0
        for i, n in enumerate(nums):
            counts[n] += 1
            diff = counts[0]-counts[1]
            if diff not in book:
                book[diff] = i
            
            if diff:
                res = max(res, i-book[diff])
            else: # balanced from start to here
                res = i+1
        return res