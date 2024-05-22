from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        ans, substrings = [], []
        def backtrack(l: int) -> None:
            if l == len(s):
                ans.append(substrings[:])
                return

            for r in range(l, len(s)):
                if is_palindrome(l, r):
                    substrings.append(s[l:r+1])
                    backtrack(r+1)
                    substrings.pop()

        backtrack(0)
        return ans