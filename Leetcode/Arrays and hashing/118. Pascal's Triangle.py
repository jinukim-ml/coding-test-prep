class Solution:
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