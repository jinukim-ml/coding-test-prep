from collections import defaultdict, Counter

class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = defaultdict(int)
        for n in self.nums2:
            self.freq[n] += 1
    
    def add(self, index: int, val: int) -> None:
        n = self.nums2[index]
        self.freq[n] -= 1
        self.nums2[index] += val
        self.freq[n+val] += 1
    
    def count(self, tot: int) -> int:
        res = 0
        for n in self.nums1:
            res += self.freq[tot-n]
        return res

class FindSumPairs: # faster solution
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums2 = nums2
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)
        self.keys = sorted(self.freq1.keys())
    
    def add(self, index: int, val: int) -> None:
        n = self.nums2[index]
        self.freq2[n] -= 1
        self.nums2[index] += val
        self.freq2[n+val] += 1
    
    def count(self, tot: int) -> int:
        res = 0
        for n in self.keys:
            if n >= tot:
                break
            if tot-n in self.freq2:
                res += self.freq1[n] * self.freq2[tot-n]
        return res