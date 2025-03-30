class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        start, end, curr = 0, 0, 0
        ans = []
        for curr in range(len(s)):
            end = max(end, last[s[curr]])
            if curr == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans

from collections import Counter, defaultdict

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        counter = Counter(s)
        curr = defaultdict(int)
        res = []
        l, r = 0, 0
        while r < len(s):
            curr[s[r]] += 1
            counter[s[r]] -= 1
            for ch in curr.keys():
                if counter[ch]:
                    break
            else:
                curr = defaultdict(int)
                res.append(r - l + 1)
                l = r + 1
            r += 1
        return res