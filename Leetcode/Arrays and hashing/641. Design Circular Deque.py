from collections import deque

class MyCircularDeque:
    def __init__(self, k: int):
        self.dq = deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.dq) < self.k:
            self.dq.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.dq) < self.k:
            self.dq.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.dq:
            self.dq.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.dq:
            self.dq.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.dq:
            return self.dq[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.dq:
            return self.dq[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def isFull(self) -> bool:
        return len(self.dq) == self.k