from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        top, bottom = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1
        
        while l <= r and top <= bottom:
            for i in range(l, r+1): # left to right
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1): # top to bottom
                ans.append(matrix[i][r])
            r -=1
            
            if not (l <= r and top <= bottom):
                break

            for i in range(r, l-1, -1): # right to left
                ans.append(matrix[bottom][i])
            bottom -= 1
            
            for i in range(bottom, top-1, -1): # bottom to top
                ans.append(matrix[i][l])
            l += 1
        
        return ans