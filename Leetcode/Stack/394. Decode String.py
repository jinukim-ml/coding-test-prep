class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                reverse_stack = []
                while stack[-1] != '[':
                    reverse_stack.append(stack.pop())
                string = ''
                while reverse_stack:
                    string += reverse_stack.pop()
                stack.pop() # left paranthesis
                number = 0
                length = 0
                while stack and stack[-1].isdigit():
                    number += int(stack.pop()) * 10**length
                    length += 1
                stack.append(number * string)
            else:
                stack.append(ch)
        return ''.join(stack)