from collections import defaultdict

class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        book = defaultdict(int)

        for start, end in intervals:
            book[start] += 1
            book[end + 1] -= 1
        
        ans, maxbooked = 0, 0
        for p in sorted(book.keys()):
            maxbooked += book[p]
            ans = max(ans, maxbooked)
        return ans