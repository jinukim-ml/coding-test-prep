class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda item: (-item[0], item[1]))
        res = 0
        for i in range(len(points)-1):
            lowest = 51
            for j in range(i+1, len(points)):
                if points[i][1] <= points[j][1] < lowest:
                    lowest = points[j][1]
                    res += 1
        return res