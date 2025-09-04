class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x2z = abs(z-x)
        y2z = abs(z-y)
        if x2z == y2z:
            return 0
        elif x2z < y2z:
            return 1
        else:
            return 2