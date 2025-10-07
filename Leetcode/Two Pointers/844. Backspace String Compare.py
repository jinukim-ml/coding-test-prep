class Solution: # two pointer solution. Time complexity: O(m+n), space complexity: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def find_valid(s: str, i: int) -> int:
            backspaces = 0
            while i >= 0:
                if s[i] == '#':
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    break
                i -= 1
            return i
        
        i, j = len(s)-1, len(t)-1
        while i >= 0 or j >= 0:
            i = find_valid(s, i)
            j = find_valid(t, j)

            ch_s = s[i] if i >= 0 else ""
            ch_t = t[j] if j >= 0 else ""            
            
            if ch_s != ch_t:
                return False
            i -= 1
            j -= 1
        return True

class Solution: # stack solution. Time complexity: O(m+n), space complexity: O(m+n)
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        for ch in s:
            if ch == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(ch)
        for ch in t:
            if ch == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(ch)
        
        return ''.join(stack_s) == ''.join(stack_t)