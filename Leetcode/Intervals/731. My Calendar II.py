from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        self.schedule = SortedDict()
        self.maxbooking = 2
    def book(self, start: int, end: int) -> bool:
        self.schedule[start] = self.schedule.get(start, 0) + 1
        self.schedule[end] = self.schedule.get(end, 0) - 1
        overlap = 0

        for cnt in self.schedule.values():
            overlap += cnt
            if overlap > self.maxbooking:
                self.schedule[start] -= 1
                self.schedule[end] += 1
            
                if self.schedule[start] == 0:
                    del self.schedule[start]
                return False
        return True