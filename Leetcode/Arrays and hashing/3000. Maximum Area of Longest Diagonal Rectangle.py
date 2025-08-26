class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        diag, res = 0, 0
        for l, w in dimensions:
            d = l*l + w*w
            if d > diag:
                diag = d
                res = l*w
            elif d == diag:
                res = max(res, l*w)
        return res