from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i], []) + [i]

        for k in table.keys():
            if target - k in table:
                if k == target - k and len(table[target - k]) > 1:
                    return[table[target - k][0], table[target - k][1]]
                elif k != target - k:
                    return[table[k][0], table[target-k][0]]