class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        arr = [(h, n) for h, n in zip(heights, names)]
        arr.sort(reverse=True)
        return [name for _, name in arr]