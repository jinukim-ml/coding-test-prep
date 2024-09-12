class Solution:
    def makeGood(self, s: str) -> str:
        lower = set([chr(97+i) for i in range(26)])
        upper = set([chr(65+i) for i in range(26)])
        stack = []        
        for ch in s:
            if stack:
                if ch in lower and stack[-1] in upper and stack[-1].lower() == ch:
                    stack.pop()
                elif ch in upper and stack[-1] in lower and stack[-1].upper() == ch:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return ''.join(stack)