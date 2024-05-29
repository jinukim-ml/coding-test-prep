import heapq

class MedianFinder:
    def __init__(self):
        # constantly split the whole array in half
        # left: max heap, right: min heap
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -heapq.heappushpop(self.right, num))
        else:
            heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] -self.left[0]) / 2
        else:
            return -self.left[0]