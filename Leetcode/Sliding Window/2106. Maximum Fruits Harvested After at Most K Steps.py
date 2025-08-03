class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        l, res = 0, 0
        window = 0
        for r in range(len(fruits)):
            window += fruits[r][1]
            cost = fruits[r][0] - fruits[l][0] + min(abs(startPos - fruits[l][0]), abs(fruits[r][0] - startPos))
            while cost > k:
                window -= fruits[l][1]
                l += 1
                if l > r:
                    break
                cost = fruits[r][0] - fruits[l][0] + min(abs(startPos - fruits[l][0]), abs(fruits[r][0] - startPos))
            res = max(res, window)
        return res