class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        zero2six = {'0','1','2','3','4','5','6'}
        zero2nine = {'0','1','2','3','4','5','6','7','8','9'}
        oneortwo = {'1','2'}

        memo = {}
        def search(idx: int) -> int:
            if idx >= len(s):
                return 1
            if s[idx] == '0':
                return 0

            if idx in memo:
                return memo[idx]

            cnt = 0
            cnt += search(idx+1)
            if idx < len(s)-1 and s[idx] in oneortwo:
                if s[idx] == '1' and s[idx+1] in zero2nine:
                    cnt += search(idx+2)
                elif s[idx] == '2' and s[idx+1] in zero2six:
                    cnt += search(idx+2)
            
            memo[idx] = cnt
            return cnt
        
        ans = 0
        ans = search(0)
        return ans