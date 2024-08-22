class Solution:
    def findComplement(self, num: int) -> int:
        comp = {'0': '1', '1': '0'}
        num = bin(num)
        n = ''.join([comp[num[i]] for i in range(2, len(num))])
        return int(n, 2)