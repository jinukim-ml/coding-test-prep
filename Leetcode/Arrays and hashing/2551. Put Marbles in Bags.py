class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        partitions = []
        for i in range(len(weights)-1):
            partitions.append((weights[i] + weights[i+1]))
        
        partitions.sort()
        res = 0
        for i in range(k-1):
            res += partitions[len(partitions)-i-1] - partitions[i]
        return res