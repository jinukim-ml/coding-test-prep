from bisect import bisect_left

class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort(key=lambda x: (x[0], x[1]))
        max_beauties = [0] * len(items)
        maxval = 0
        for i, (p, b) in enumerate(items):
            maxval = max(maxval, b)
            max_beauties[i] = maxval

        answer = []
        for q in queries:
            i = bisect_left(items, [q,float('inf')])
            if i == 0:
                answer.append(0)
            else:
                answer.append(max_beauties[i-1])
        return answer