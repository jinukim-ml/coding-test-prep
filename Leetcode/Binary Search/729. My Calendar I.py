from bisect import bisect_left

class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if not self.calendar:
            self.calendar.append((start, end))
            return True
        
        idx = bisect_left(self.calendar, start, key= lambda x: x[0])
        if 0 < idx < len(self.calendar):
            if self.calendar[idx-1][1] <= start and end <= self.calendar[idx][0]:
                self.calendar.insert(idx, (start, end))
                return True
            else:
                return False
        elif idx == 0:
            if end <= self.calendar[idx][0]:
                self.calendar.insert(0, (start, end))
                return True
            else:
                return False
        elif idx == len(self.calendar):
            if self.calendar[idx-1][1] <= start:
                self.calendar.append((start, end))
                return True
            else:
                return False