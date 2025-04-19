class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        i, j = 0, 0
        while i < len(pushed) and j < len(popped):
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                continue
            
            stack.append(pushed[i])
            i += 1
        while j < len(popped) and stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        if stack:
            return False
        return True