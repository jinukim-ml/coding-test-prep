class Solution: # factorial
    def generate(self, numRows: int) -> list[list[int]]:
        table = {}
        def factorial(target):
            if target in table:
                return table[target]
            res = 1
            for i in range(2, target+1):
                res *= i
            table[target] = res
            return res
        ans = []
        for n in range(numRows):
            row = []
            for k in range(n+1):
                row.append(factorial(n) // (factorial(k)*factorial(n-k)))
            ans.append(row)
        
        return ans
    
class Solution: # DP
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for i in range(2, numRows+1):
            row = [1]
            for j in range(1, i-1):
                val = res[-1][j-1] + res[-1][j]
                row.append(val)
            row.append(1)
            res.append(row)
        return res