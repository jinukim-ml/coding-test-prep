class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        operators = set(['!', '&', '|'])
        valid = set(['!', '&', '|', 't', 'f'])
        for ch in expression:
            if ch in valid:
                stack.append(ch)
            elif ch == ')':
                has_t, has_f = False, False
                while stack[-1] not in operators:
                    op = stack.pop()
                    if op == 't':
                        has_t = True
                    else:
                        has_f = True

                op = stack.pop()
                if op == '!': # not
                    stack.append('t' if has_f else 'f')
                elif op == '&': # and
                    stack.append('f' if has_f else 't')
                else: # or
                    stack.append('t' if has_t else 'f')
        return stack[0] == 't'