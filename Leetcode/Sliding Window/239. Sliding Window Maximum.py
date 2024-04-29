from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        nswer = []

        l = 0
        # our deque is a decreasing monotonic queue.
        # the first element in the queue is the largest in the queue and the last is the smallest.
        # when a new element is added, we compare it with the last element of the queue.
        # we remove elements from the end of the queue until the last queue element is larger than the new window element or the queue becomes empty.
        for r in range(len(nums)):
            if r - l + 1 > k:
                if nums[l] == dq[0]:
                    dq.popleft()
                l += 1
            while dq and dq[-1] < nums[r]:
                dq.pop()
            dq.append(nums[r])
            
            # print(f'r: {r}, nums[r]: {nums[r]}, dq: {dq}')
            if r >= k-1:
                nswer.append(dq[0])
        return nswer