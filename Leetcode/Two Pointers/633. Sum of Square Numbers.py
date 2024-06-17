class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start, end = 0, int(c ** 0.5)
        while start <= end:
            s = start ** 2 + end ** 2
            if s < c:
                start += 1
            elif s > c:
                end -= 1
            else:
                return True
        return False