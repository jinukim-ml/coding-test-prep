class Solution: # solution using string
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for n1 in range(1, n):
            if '0' in str(n1):
                continue
            n2 = n - n1
            if '0' not in str(n2):
                return [n1, n2]

class Solution: # solution without using string
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for n1 in range(1, n):
            x = n1
            while x:
                x, r = divmod(x, 10)
                if r == 0:
                    break
            else:
                n2 = n - n1
                x = n2
                while x:
                    x, r = divmod(x, 10)
                    if r == 0:
                        break
                else:
                    return [n1, n2]