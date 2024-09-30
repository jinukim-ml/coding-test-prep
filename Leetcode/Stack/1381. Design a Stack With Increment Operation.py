class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxsize = maxSize
        self.increments = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxsize:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if not self.stack:
            return - 1
        
        if len(self.increments) > 1:
            self.increments[-2] += self.increments[-1]
        return self.stack.pop() + self.increments.pop()

    def increment(self, k: int, val: int) -> None:
        if self.increments:
            self.increments[min(k, len(self.increments)) - 1] += val