class Solution: # prefix sum
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        prefix = [0 for _ in range(n)]
        for i in reversed(range(n)):
            prefix[i] = energy[i]
            if i+k < n:
                prefix[i] += prefix[i+k]
        
        res = -1001
        for i in range(n):
            res = max(res, prefix[i])
        return res

class Solution: # dynamic programming
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        for i in range(n-k-1, -1, -1):
            energy[i] += energy[i+k]
        return max(energy)