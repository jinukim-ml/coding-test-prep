class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(s: str, target: int) -> bool:
            if s == "" and target == 0:
                return True
            if target < 0:
                return False
            
            for i in range(len(s)):
                left = s[:i+1]
                right = s[i+1:]
                if backtrack(right, target - int(left)):
                    return True
            return False
        
        res = 0
        for i in range(1, n+1):
            squared = i*i
            if backtrack(str(squared), i):
                res += squared
        return res