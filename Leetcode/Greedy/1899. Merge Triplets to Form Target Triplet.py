from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        indices = []
        x,y,z = -1, -1, -1 # indices
        for i, (a,b,c) in enumerate(triplets):
            if a <= target[0] and b <= target[1] and c <= target[2]:
                indices.append(i)
                if a == target[0]:
                    x = i
                if b == target[1]:
                    y = i
                if c == target[2]:
                    z = i
        
        if not indices or x == -1 or y == -1 or z == -1:
            return False
        return True

class Solution: # Another solution. Similar performance
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        s = set()
        for i, (a,b,c) in enumerate(triplets):
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            if a == target[0]:
                s.add(0)
            if b == target[1]:
                s.add(1)
            if c == target[2]:
                s.add(2)
        
        return len(s) == 3