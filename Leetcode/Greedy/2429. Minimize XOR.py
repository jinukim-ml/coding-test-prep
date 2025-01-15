class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin1 = bin(num1)[2:]
        ones1 = bin1.count('1')
        bin2 = bin(num2)[2:]
        ones2 = bin2.count('1')
        
        if ones1 == ones2:
            return num1
        elif ones1 > ones2:
            res = ['0'] * len(bin1)
            cnt, i = 0, 0
            while cnt < ones2:
                if bin1[i] == '1':
                    res[i] = '1'
                    cnt += 1
                i += 1
            res = int(''.join(res), 2)
            return res
        else:
            if len(bin1) >= len(bin2):
                res = ['0'] * len(bin1)
                cnt, i = 0, 0
                while cnt < ones1:
                    if bin1[i] == '1':
                        res[i] = '1'
                        cnt += 1
                    i += 1
                
                i = len(bin1)-1
                while cnt < ones2:
                    if res[i] == '0':
                        res[i] = '1'
                        cnt += 1
                    i -= 1
            else: # len(bin1) < len(bin2)
                res = ['0'] * len(bin2)
                cnt, i = 0, len(bin2)-len(bin1)

                while cnt < ones1:
                    if bin1[i - len(bin2) + len(bin1)] == '1':
                        res[i] = '1'
                        cnt += 1
                    i += 1
                i = len(bin2)-1
                while cnt < ones2:
                    if res[i] == '0':
                        res[i] = '1'
                        cnt += 1
                    i -= 1
            return int(''.join(res), 2)