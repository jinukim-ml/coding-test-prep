class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ordered = sorted(list(set(arr)))
        book = {}

        for i, n in enumerate(ordered):
            book[n] = i+1
        
        ans = []
        for n in arr:
            ans.append(book[n])
        return ans