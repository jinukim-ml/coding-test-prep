class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        recolored = 0
        res = float('inf')
        while r < len(blocks):
            if blocks[r] == 'W':
                recolored += 1
            if r - l + 1 == k:
                res = min(res, recolored)
                if blocks[l] == 'W':
                    recolored -= 1
                l += 1
            r += 1
        return res