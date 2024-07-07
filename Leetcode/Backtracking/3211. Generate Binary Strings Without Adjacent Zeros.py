from typing import List
from functools import cache

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ['0', '1']
        
        seen = set()
        ans = []
        @cache
        def backtracking(i:int, string:str):
            if i >= n:
                ans.append(string)
                seen.add(string)
                return
            
            if len(string) and string[-1] == '1':
                backtracking(i+1, string+'0')
            backtracking(i+1, string+'1')
        
        backtracking(1, '0')
        backtracking(0, '')
        return ans