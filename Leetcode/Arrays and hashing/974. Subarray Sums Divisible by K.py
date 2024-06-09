from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        hashmap = {0:1}

        ans = 0
        for n in nums:
            prefix += n
            mod = prefix % k
            if mod in hashmap:
                print(f'mod: {mod}, hashmap[mod]: {hashmap[mod]}')
                ans += hashmap[mod]
                hashmap[mod] += 1
            else:
                hashmap[mod] = 1
        return ans