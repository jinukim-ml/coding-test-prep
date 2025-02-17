from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        curr = {chr(i+65): 0 for i in range(26)}
        seen = set()
        def backtrack(s: str) -> None:
            seen.add(s)
            for k, v in cnt.items():
                if curr[k] < v:
                    curr[k] += 1
                    backtrack(s + k)
                    curr[k] -= 1
        backtrack(s="")
        return len(seen)-1