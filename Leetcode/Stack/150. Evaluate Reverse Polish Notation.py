from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for data in tokens:
            if data not in ops:
                stack.append(int(data))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if data == '+':
                    stack.append(operand1 + operand2)
                elif data == '-':
                    stack.append(operand1 - operand2)
                elif data == '*':
                    stack.append(operand1 * operand2)
                elif data == '/':
                    stack.append(int(operand1/operand2))
        
        return stack.pop()