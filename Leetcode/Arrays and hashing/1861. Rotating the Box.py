class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        m, n = len(box), len(box[0])
        for row in range(m):
            stones = []
            for right in range(n):
                if box[row][right] == '#': # stone
                    stones.append(right)
                elif box[row][right] == '*': # obstacle
                    cursor = right - 1
                    while len(stones) > 0:
                        idx = stones.pop()
                        box[row][cursor], box[row][idx] = box[row][idx], box[row][cursor]
                        cursor -= 1
                    stones = []
            # gravity
            cursor = n - 1
            while len(stones) > 0:
                idx = stones.pop()
                box[row][cursor], box[row][idx] = box[row][idx], box[row][cursor]
                cursor -= 1

        ans = [[None for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                ans[c][m-r-1] = box[r][c]
        return ans