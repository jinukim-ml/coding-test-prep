class Solution:
    def fractionAddition(self, expression: str) -> str:
        ops = {'+': 1, '-': -1}
        # a1/a2 + b1/b2
        if expression[0] == '-':
            sign = -1
            cur = 1
        else:
            sign = 1
            cur = 0

        while cur < len(expression) and expression[cur] not in ops:
            a1 = sign * int(expression[cur])
            cur += 1
            if expression[cur] != '/':
                a1 *= 10
                cur += 1
            cur += 1
            
            a2 = int(expression[cur])
            cur += 1
            if cur < len(expression) and expression[cur] not in ops:
                a2 = 10
                cur += 1

        while cur < len(expression):
            sign = ops[expression[cur]]
            cur += 1

            b1 = sign * int(expression[cur])
            cur += 1
            if expression[cur] != '/':
                b1 *= 10
                cur += 1
            cur += 1

            b2 = int(expression[cur])
            cur += 1
            if cur < len(expression) and expression[cur] not in ops:
                b2 *= 10
                cur += 1

            if a2 == b2:
                a1 += b1
            elif a2 > b2:
                q = a2 / b2
                if int(q) == q:
                    a1 += b1 * q
                else:
                    # numerator
                    a1 *= b2
                    a1 += b1 * a2
                    # denominator
                    a2 *= b2
            else:
                q = b2 / a2
                if int(q) == q:
                    # numerator
                    a1 *= q
                    a1 += b1
                    # denominator
                    a2 = b2
                else:
                    # numerator
                    a1 *= b2
                    a1 += b1 * a2
                    # denominator
                    a2 *= b2
        
        a1 = int(a1)
        ans = ''
        if a1 < 0:
            a1 *= -1
            ans += '-'
        elif a1 == 0:
            return '0/1'
        
        for x in range(min(a1,a2)+1, 1, -1):
            q1, q2 = a1 / x, a2 / x
            if int(q1) == q1 and int(q2) == q2:
                a1 //= x
                a2 //= x
        return ans + str(a1) + '/' + str(a2)