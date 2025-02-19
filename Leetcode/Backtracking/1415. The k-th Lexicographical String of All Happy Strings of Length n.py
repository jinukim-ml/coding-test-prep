class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        candidates = ['a', 'b', 'c']
        cnt = 0
        res = []
        def backtrack(i: int) -> bool:
            if i == n:
                nonlocal cnt
                cnt += 1
                if cnt == k:
                    return True
                else:
                    return False
            
            for ch in candidates:
                if ch != res[-1]:
                    res.append(ch)
                    if backtrack(i+1):
                        return True
                    res.pop()
            return False
        
        for ch in candidates:
            res.append(ch)
            if backtrack(1):
                break
            res.pop()
        return ''.join(res)