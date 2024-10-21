class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(i: int, seen: set) -> None:
            if i == len(s):
                return 0
            splits = 0
            for r in range(i+1, len(s)+1):
                string = s[i:r]
                if string not in seen:
                    seen.add(string)
                    splits = max(splits, 1 + backtrack(r, seen))
                    seen.remove(string)
            return splits
        return backtrack(0, set())