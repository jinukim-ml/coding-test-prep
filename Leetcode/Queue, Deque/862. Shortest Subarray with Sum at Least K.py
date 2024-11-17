from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        
        shortest = float('inf')
        dq = deque() # monotonic deque

        for i in range(len(prefix)):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                shortest = min(shortest, i - dq.popleft())
            
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        if shortest == float('inf'):
            return -1
        else:
            return shortest