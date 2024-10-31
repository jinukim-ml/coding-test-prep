class Solution: # Bottom-up DP
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda pair: pair[0])

        fpos = []
        for pos, cap in factory:
            for _ in range(cap):
                fpos.append(pos)
        
        rcnt, fcnt = len(robot), len(fpos)
        dp = [[0] * (fcnt+1) for _ in range(rcnt+1)]

        for i in range(rcnt):
            dp[i][fcnt] = float('inf')
        
        for i in range(rcnt-1, -1, -1):
            for j in range(fcnt-1, -1, -1):
                assign = abs(robot[i] - fpos[j]) + dp[i+1][j+1]
                skip = dp[i][j+1]
                dp[i][j] = min(assign, skip)
        return dp[0][0]
    
class Solution: # Top-down DP + memoization
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda pair: pair[0])

        fpos = []
        for f, c in factory:
            fpos += [f] * c
        
        dp = [[-1] * (len(fpos)+1) for _ in range(len(robot)+1)]
        
        def mindist(r: int, f: int) -> int:
            if dp[r][f] != -1:
                return dp[r][f]
            if r == len(robot):
                dp[r][f] = 0
                return 0
            if f == len(fpos):
                dp[r][f] = float('inf')
                return float('inf')

            assign = abs(robot[r] - fpos[f]) + mindist(r+1, f+1)
            skip = mindist(r, f+1)
            dp[r][f] = min(assign, skip)
            return dp[r][f]
        return mindist(0, 0)