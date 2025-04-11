class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for x in range(low, high+1):
            num = str(x)
            if len(num)%2:
                continue
            left = 0
            for i in range(len(num)//2):
                left += int(num[i])
            right = 0
            for i in range(len(num)//2, len(num)):
                right += int(num[i])
            if left == right:
                res += 1
        return res