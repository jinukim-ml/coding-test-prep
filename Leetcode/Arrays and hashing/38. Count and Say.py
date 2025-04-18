# recursive solution
class Solution:
    def countAndSay(self, n: int) -> str:
        def recursion(step: int, s: str) -> str:
            res = ''
            j = 0
            while j < len(s):
                k = j
                while k < len(s)-1 and s[k] == s[k+1]:
                    k += 1
                res += str(k - j + 1) + s[k]
                j = k+1
            if step == n:
                return res
            return recursion(step+1, res)
        if n == 1:
            return '1'
        return recursion(2, '1')

# iterative solution
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n-1):
            s = ''
            i = 0
            while i < len(res):
                j = i
                while j < len(res)-1 and res[j] == res[j+1]:
                    j += 1
                s += str(j - i + 1) + res[j]
                i = j + 1
            res = s
        return res