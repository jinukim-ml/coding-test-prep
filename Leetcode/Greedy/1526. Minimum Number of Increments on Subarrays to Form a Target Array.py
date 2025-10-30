class Solution: # O(n^2). this won't pass because of MLE :(
    def minNumberOperations(self, target: list[int]) -> int:
        if not target:
            return 0
        minval = min(target)
        l, r = 0, len(target)-1
        for i in range(len(target)):
            target[i] -= minval
            if target[i] == 0 and i < r:
                r = i
        return minval + self.minNumberOperations(target[l:r]) + self.minNumberOperations(target[r+1:])

class Solution: # O(n) greedy
    def minNumberOperations(self, target: list[int]) -> int:
        res = target[0]        
        for i in range(1, len(target)):
            diff = target[i] - target[i-1]
            if diff > 0:
                res += diff
        return res