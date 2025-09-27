class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        res = 0
        for i in range(len(points)-2):
            x1, y1 = points[i]
            for j in range(i+1, len(points)-1):
                x2, y2 = points[j]
                for k in range(j+1, len(points)):
                    x3, y3 = points[k]
                    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
                    res = max(res, area)
        return res