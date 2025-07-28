class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        target = nums[0]
        for i, n in enumerate(nums):
            target = max(target, target|n)

        ans = 0
        def backtrack(i: int, val: int) -> None:
            if i == len(nums):
                return
            nonlocal ans

            backtrack(i+1, val)

            val |= nums[i]
            if val == target:
                ans += 1
            backtrack(i+1, val)
        
        backtrack(0, 0)
        return ans

class Solution: # solution #2
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        pair = [0, 0]
        def backtrack(i: int, val: int):
            if i == len(nums):
                if val > pair[0]:
                    pair[0] = val
                    pair[1] = 1
                elif val == pair[0]:
                    pair[1] += 1
                return
            backtrack(i+1, val|nums[i])
            backtrack(i+1, val)
        backtrack(0, 0)
        return pair[1]