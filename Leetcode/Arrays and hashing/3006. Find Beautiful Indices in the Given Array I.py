class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        def verify(start: int, string: str) -> bool:
            return s[start:start+len(string)] == string
        res = []
        group_i, group_j = [], []
        for i in range(len(s)):
            if verify(i, a):
                group_i.append(i)
            if verify(i, b):
                group_j.append(i)
        for i in group_i:
            for j in group_j:
                if abs(i-j) <= k:
                    res.append(i)
                    break
        return res