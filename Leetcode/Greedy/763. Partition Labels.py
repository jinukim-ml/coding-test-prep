from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        start, end, curr = 0, 0, 0
        ans = []
        while curr < len(s):
            end = max(end, last[s[curr]])
            if curr == end:
                ans.append(end - start + 1)
                start = end + 1
                curr = start
            else:
                curr += 1
        return ans