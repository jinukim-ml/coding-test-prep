class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        nums = [intervals[0][1]-1, intervals[0][1]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if nums[-1] < s:
                nums.append(e-1)
                nums.append(e)
            elif nums[-2] < s:
                nums.append(e)
        return len(nums)