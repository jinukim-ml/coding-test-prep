class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # numBottles: the number of full water bottles
        empty, res = 0, 0
        while True:
            if empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                if numBottles == 0:
                    break
                empty += numBottles
                res += numBottles
                numBottles = 0
        return res