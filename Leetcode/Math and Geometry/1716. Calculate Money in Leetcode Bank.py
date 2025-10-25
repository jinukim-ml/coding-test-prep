class Solution:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        return 28*q + 7*(q-1)*q//2 + r*(2*q+r+1)//2
    
class Solution: # brute force
    def totalMoney(self, n: int) -> int:
        res, bonus = 0, 0
        arr = [i for i in range(7)]
        arr[0] = 7
        for i in range(1, n+1):
            res += arr[i%7] + bonus
            if i%7 == 0:
                bonus += 1
        return res