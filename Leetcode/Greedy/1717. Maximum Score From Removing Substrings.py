class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y:
            higher = 'ab'
            lower = 'ba'
            score = [x, y]
        else:
            higher = 'ba'
            lower = 'ab'
            score = [y, x]
        
        n = len(s)
        s = self.delete(s, higher)
        ans = (n - len(s)) // 2 * score[0]

        n = len(s)
        s = self.delete(s, lower)
        ans += (n - len(s)) // 2 * score[1]
        return ans
    
    def delete(self, s: str, target: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == target[0] and ch == target[1]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)