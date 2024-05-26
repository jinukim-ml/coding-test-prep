from bisect import bisect_left

class TimeMap:
    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = [(value, timestamp)]
        else:
            idx = bisect_left(self.table[key], timestamp, key=lambda item: item[1])
            self.table[key].insert(idx, (value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        
        idx = bisect_left(self.table[key], timestamp, key=lambda item: item[1])
        if idx >= len(self.table[key]):
            return self.table[key][-1][0]
        else:
            if self.table[key][idx][1] > timestamp:
                if idx == 0:
                    return ""
                else:
                    return self.table[key][idx-1][0]
            else:
                return self.table[key][idx][0]