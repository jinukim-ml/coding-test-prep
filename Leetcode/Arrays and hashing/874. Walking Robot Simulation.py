class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        blocked = set()
        for x, y in obstacles:
            blocked.add((x,y))

        maxdist = 0
        directions = [(0,1), (-1,0), (0,-1), (1,0)]
        facing = 0
        pos = [0, 0]
        for c in commands:
            if c == -2:
                facing = (facing+1)%4
            elif c == -1:
                facing = (facing-1)%4
            else:
                dx, dy = directions[facing][0], directions[facing][1]
                # obstacle check
                for _ in range(c):
                    x, y = pos
                    if (x + dx, y + dy) in blocked:
                        break
                    else:
                        pos = [x + dx, y + dy]
                newdist = pos[0]**2 + pos[1]**2
                maxdist = max(maxdist, newdist)
        return maxdist