class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        players = [[0 for __ in range(11)] for _ in range(n)]

        for x, y in pick:
            players[x][y] += 1

        ans = 0
        for i in players[0]:
            if i >= 1:
                ans += 1
                break

        for i in range(1, n):
            for j in range(11):
                if players[i][j] >= i+1:
                    ans += 1
                    break
        return ans