from collections import defaultdict
import heapq

class NumberContainers:
    def __init__(self):
        self.container = {}
        self.indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        heapq.heappush(self.indices[number], index)
    
    def find(self, number: int) -> int:
        if number not in self.indices:
            return -1
        while self.indices[number]:
            i = self.indices[number][0]
            if self.container[i] == number:
                return i
            heapq.heappop(self.indices[number])
        return -1