from collections import Counter
class Solution: # brute force
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        digits.sort()
        cnt = Counter(digits)
        evens = {k: v for k, v in cnt.items() if k&1==0}
        res = []
        for first in cnt.keys():
            if first == 0:
                continue
            cnt[first] -= 1
            if first&1 == 0:
                evens[first] -= 1
            for second in cnt.keys():
                if cnt[second] == 0:
                    continue
                if second in evens:
                    evens[second] -= 1
                for third in evens.keys():
                    if evens[third] > 0:
                        res.append(first*100 + second*10 + third)
                if second in evens:
                    evens[second] += 1
            cnt[first] += 1
            if first&1 == 0:
                evens[first] += 1
        return res

class Solution: # slower solution
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        cnt = Counter(digits)
        res = []
        for i in range(100, 999, 2):
            nums = []
            n = i
            while n:
                n, r = divmod(n, 10)
                nums.append(r)
            for x in nums:
                cnt[x] -= 1
            if cnt[nums[0]] >= 0 and cnt[nums[1]] >= 0 and cnt[nums[2]] >= 0:
                res.append(i)
            for x in nums:
                cnt[x] += 1
        return res