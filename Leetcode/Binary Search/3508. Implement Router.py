from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

class Router:
    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.maxlen = memoryLimit
        self.hashset = set()
        self.hashmap = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.hashset:
            return False
        if len(self.q) == self.maxlen:
            self.forwardPacket()
        self.q.append((source,destination,timestamp))
        self.hashset.add((source,destination,timestamp))
        self.hashmap[destination].append(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.hashset.remove((s,d,t))
        self.hashmap[d].popleft()
        return [s,d,t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if not self.hashmap[destination]:
            return 0
        l = bisect_left(self.hashmap[destination], startTime)
        r = bisect_right(self.hashmap[destination], endTime)
        return r - l