from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        l, total = 0, 0
        freq = Counter()
        res = []
        for r in range(len(nums)):
            freq[nums[r]] += 1
            total += nums[r]
            if r-l+1 == k:
                if len(freq.keys()) < x:
                    res.append(total)
                else:
                    arr = sorted(list(freq.items()), key=lambda  x: (x[1], x[0]), reverse=True)
                    val = 0
                    for i in range(x):
                        val += arr[i][0] * arr[i][1]
                    res.append(val)
                freq[nums[l]] -= 1
                total -= nums[l]
                l += 1
        return res