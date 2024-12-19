class Solution: # O(n) monotonic stack
    def maxChunksToSorted(self, arr: list[int]) -> int:
        stack = []
        for n in arr:
            if stack and stack[-1] > n:
                maximum = stack[-1]
                while stack and n < stack[-1]:
                    stack.pop()
                stack.append(maximum)
            else:
                stack.append(n)
        return len(stack)

class Solution: # O(n) solution using running sum
    def maxChunksToSorted(self, arr: list[int]) -> int:
        # at arr[i], running sum should be i*(i+1)/2 if it is sorted
        # the number of matches -> the number of partitions (chunks)
        running_sum = 0
        res = 0
        for i in range(len(arr)):
            running_sum += arr[i]
            if running_sum == i * (i+1) / 2:
                res += 1
        return res