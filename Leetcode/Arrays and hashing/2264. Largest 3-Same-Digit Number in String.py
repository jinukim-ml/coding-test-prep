class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        x = -1
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i] and int(num[i]) > x:
                res = num[i-2:i+1]
                x = int(num[i])
        return res