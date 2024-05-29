from typing import List
from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        t = 0
        q = deque()

        while maxheap or q:
            t += 1
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt: # is cnt nonzero?
                    q.append([cnt, t+n]) # (remaining tasks, next available time)
            else:
                t = q[0][1] # skip the wating
            
            if q and q[0][1] == t:
                heapq.heappush(maxheap, q.popleft()[0])
        
        return t