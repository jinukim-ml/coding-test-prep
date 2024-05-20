from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0] * (len(nums)+1)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]
            if (nums[i]%2) == (nums[i-1]%2):
                prefix[i] += 1

        ans = []
        for start, end in queries:
            if start == end:
                ans.append(True)
            else:
                if prefix[end] - prefix[start] > 0:
                    ans.append(False)
                else:
                    ans.append(True)
        
        return ans