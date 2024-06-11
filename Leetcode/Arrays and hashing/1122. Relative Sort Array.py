from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []
        for n in arr2:
            if n in cnt:
                for _ in range(cnt[n]):
                    ans.append(n)
                cnt.pop(n)
        for k in sorted(cnt.keys()):
            for _ in range(cnt[k]):
                ans.append(k)
        return ans