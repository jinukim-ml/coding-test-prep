from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, subarray = [], ["("]

        def backtrack(l, r):
            if len(subarray) == 2*n:
                ans.append("".join(subarray))
                return
            
            if l < n:
                subarray.append("(")
                backtrack(l+1, r)
                subarray.pop()

            if r < l:
                subarray.append(")")
                backtrack(l, r+1)
                subarray.pop()
        
        backtrack(1, 0)
        return ans