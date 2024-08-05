from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        ans = ''
        book = Counter(arr)

        cnt = 0
        for s in arr:
            if book[s] == 1:
                cnt += 1
                if cnt == k:
                    ans = s
        return ans