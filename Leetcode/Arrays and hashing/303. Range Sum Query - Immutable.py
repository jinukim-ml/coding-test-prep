class NumArray:
    def __init__(self, nums: list[int]):
        self.arr = nums
        running_sum = 0
        self.prefix = [0]
        for i in range(len(self.arr)):
            running_sum += self.arr[i]
            self.prefix.append(running_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]