from collections import Counter
class Solution: # one-liner. O(nlogn)
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(list(Counter(nums).items()), key=lambda x: x[1], reverse=True)[0][0]

class Solution: # time complexity O(n), space complexity O(1)
    def majorityElement(self, nums: list[int]) -> int:
        ans = None
        cnt = 0
        for n in nums:
            if cnt == 0:
                ans = n
            if ans == n:
                cnt += 1
            else:
                cnt -= 1
        return ans