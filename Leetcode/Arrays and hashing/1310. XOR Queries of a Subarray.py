class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        precalc = []
        xor = 0
        for item in arr:
            xor ^= item
            precalc.append(xor)
        
        ans = []
        for l, r in queries:
            if l > 0:
                ans.append(precalc[l-1] ^ precalc[r])
            else:
                ans.append(precalc[r])
        return ans