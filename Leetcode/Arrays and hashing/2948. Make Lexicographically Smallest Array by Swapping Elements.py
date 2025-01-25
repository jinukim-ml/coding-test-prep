class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        sorted_num = sorted((n, i) for i, n in enumerate(nums))

        new = []
        curr = []
        prev = float('-inf')
        for n, i in sorted_num:
            if n > prev + limit:
                new += sorted(curr)
                curr = [i]
            else:
                curr.append(i)
            prev = n
        
        new += sorted(curr)
        res = [0] * len(nums)
        for i, pos in enumerate(new):
            res[pos] = sorted_num[i][0]
        return res