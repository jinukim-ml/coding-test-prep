from collections import Counter, defaultdict
import heapq

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        freqmap = defaultdict(list)
        for val, freq in cnt.items():
            heapq.heappush(freqmap[freq], -val)

        ans = []
        for freq in sorted(freqmap.keys()):
            while freqmap[freq]:
                val = -heapq.heappop(freqmap[freq])
                ans += [val] * freq
        return ans