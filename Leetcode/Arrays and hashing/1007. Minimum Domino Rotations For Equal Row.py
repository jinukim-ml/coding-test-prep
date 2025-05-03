class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        res = float('inf')
        for val in range(1, 7):
            top_swaps, bottom_swaps = 0, 0
            for i in range(len(tops)):
                if tops[i] != val and bottoms[i] != val:
                    break
                if tops[i] != val:
                    top_swaps += 1
                if bottoms[i] != val:
                    bottom_swaps += 1
            else:
                res = min(res, top_swaps, bottom_swaps)
        
        if res == float('inf'):
            return -1
        return res