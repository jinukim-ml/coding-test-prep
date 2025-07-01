class Solution: # simple solution
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                res += 1
        return res

class Solution: # stack solution
    def possibleStringCount(self, word: str) -> int:
        res = 1
        stack = []
        for ch in word:
            if not stack or stack[-1] == ch:
                stack.append(ch)
            else:
                res += len(stack)-1
                stack = [ch]
        res += len(stack)-1
        return res