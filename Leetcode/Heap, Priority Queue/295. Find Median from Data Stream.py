import heapq, math

class MedianFinder:
    def __init__(self):
        self.length = 0
        self.left, self.right = [], []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        self.length += 1
        # constantly split the whole array in half
        # left: max heap, right: min heap
        if not self.left: # both are empty
            heapq.heappush(self.left, -num)
        elif not self.right: # right half is empty
            if num >= -self.left[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.right, -heapq.heappop(self.left))
                heapq.heappush(self.left, -num)
        else: # both not empty
            if num < -self.left[0]:
                heapq.heappush(self.left, -num)
                while len(self.left) > math.ceil(self.length/2):
                    heapq.heappush(self.right, -heapq.heappop(self.left))
            else:
                heapq.heappush(self.right, num)
                while len(self.left) < math.ceil(self.length/2):
                    heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if (len(self.left)+len(self.right)) % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]