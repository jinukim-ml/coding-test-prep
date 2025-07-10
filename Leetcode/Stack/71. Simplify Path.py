class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        depth = 0
        path = path.split('/')
        for ch in path:
            if ch == '.' or ch == '':
                continue
            elif ch == '..':
                if depth > 0:
                    stack.pop()
                    stack.pop()
                    depth -= 1
            else:
                stack.append(ch)
                stack.append('/')
                depth += 1
        
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        return ''.join(stack)