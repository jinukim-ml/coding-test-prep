class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}
        return self.get_res(expression, memo, 0, len(expression)-1)
    
    def get_res(self, expression: str, memo: dict, start: int, end: int) -> list[int]:
        if (start, end) in memo:
            return memo[(start, end)]
        
        res = []

        if start == end:
            res.append((int(expression[start])))
            return res
        
        if end - start == 1 and expression[start].isdigit():
            res.append(int(expression[start:end+1]))
            return res
        
        for i in range(start, end+1):
            if expression[i].isdigit():
                continue
            
            left = self.get_res(expression, memo, start, i-1)
            right = self.get_res(expression, memo, i+1, end)

            for l_val in left:
                for r_val in right:
                    if expression[i] == '+':
                        res.append(l_val + r_val)
                    elif expression[i] == '-':
                        res.append(l_val - r_val)
                    elif expression[i] == '*':
                        res.append(l_val * r_val)
        
        memo[(start, end)] = res
        return res