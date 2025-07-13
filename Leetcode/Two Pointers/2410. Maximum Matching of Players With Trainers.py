class Solution: # more streamlined approach
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        for t in trainers:
            if t >= players[res]:
                res += 1
                if res == len(players):
                    break
        return res

class Solution: # two pointers
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        p1, p2, res = 0, 0, 0
        while p1 < len(players) and p2 < len(trainers):
            while p2 < len(players) and players[p1] > trainers[p2]:
                p2 += 1
            if p2 < len(trainers) and players[p1] <= trainers[p2]:
                p1 += 1
                p2 += 1
                res += 1
            else:
                p2 += 1
        return res