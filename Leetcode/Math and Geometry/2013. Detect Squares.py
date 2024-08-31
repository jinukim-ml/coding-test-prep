from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.pts = []
        self.ptscount = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.pts.append(point)
        self.ptscount[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        ans = 0

        for px, py in self.pts:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            ans += self.ptscount[(x, py)] * self.ptscount[(px, y)]
        return ans