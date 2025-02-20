class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        seen = set(nums)
        res = ''
        def backtrack(s: str, i: int) -> bool:
            if i == len(nums):
                if s in seen: 
                    return False
                else:
                    nonlocal res
                    res = s
                    return True
            
            for ch in ['0', '1']:
                if backtrack(s + ch, i+1):
                    return True
            return False
        backtrack('', 0)
        return res