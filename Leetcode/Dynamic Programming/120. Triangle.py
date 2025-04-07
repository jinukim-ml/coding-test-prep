class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        prev = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(prev[j], prev[j+1])
            prev = triangle[i]
        return triangle[0][0]