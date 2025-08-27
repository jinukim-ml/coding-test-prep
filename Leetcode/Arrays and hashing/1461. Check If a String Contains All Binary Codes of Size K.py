class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bins = set()
        for i in range(len(s)-k+1):
            bins.add(s[i:i+k])
        return len(bins) == 2**k