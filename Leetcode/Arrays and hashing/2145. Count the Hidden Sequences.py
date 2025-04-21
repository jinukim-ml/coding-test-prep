class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        smallest, largest = 0, 0
        curr = 0
        for d in differences:
            curr += d
            smallest = min(smallest, curr)
            largest = max(largest, curr)
            if largest - smallest > upper - lower:
                return 0
        return upper - lower - largest + smallest + 1