from typing import List
class Solution: # two pointers solution
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
        
        return [left+1, right+1]

class Solution2: # solution using hashing
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(numbers)):
            table[numbers[i]] = table.get(numbers[i], []) + [i]

        for x in table:
            if target - x in table and x != target-x:
                if x != target - x:
                    return sorted([table[x][0]+1, table[target-x][0]+1])
            elif target - x  == x and len(table[x]) > 1:
                return [table[x][0]+1, table[x][1]+1]