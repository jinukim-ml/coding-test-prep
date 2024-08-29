from collections import defaultdict

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        self.rows, self.cols =  defaultdict(list[int]), defaultdict(list[int])
        self.points = set()
        for x, y in stones:
            self.rows[x].append(y)
            self.cols[y].append(x)
            self.points.add((x,y))
        
        num_clusters = 0
        for x, y in stones:
            if (x, y) in self.points:
                self.remove_point(x,y)
                num_clusters += 1
        
        return len(stones) - num_clusters
    
    def remove_point(self, x: int, y: int) -> None:
        self.points.discard((x,y))
        for y_ in self.rows[x]:
            if (x, y_) in self.points:
                self.remove_point(x, y_)
        
        for x_ in self.cols[y]:
            if (x_, y) in self.points:
                self.remove_point(x_, y)