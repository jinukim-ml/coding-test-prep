from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        table = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        ans = []
        def backtrack(i: int, string: str):
            if i == len(digits):
                ans.append(string)
                return
            
            for j in range(len(table[digits[i]])):
                backtrack(i+1, string + table[digits[i]][j])
        
        backtrack(0, '')
        return ans