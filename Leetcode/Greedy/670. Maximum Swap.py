class Solution: # O(n)
    def maximumSwap(self, num: int) -> int:
        num_l = list(str(num))
        digits = {int(n): i for i, n in enumerate(num_l)}
        
        for i in range(len(num_l)):
            for n in range(9, int(num_l[i]), -1):
                idx = digits.get(n, -1)
                if idx > i:
                    num_l[i], num_l[idx] = num_l[idx], num_l[i]
                    return int(''.join(num_l))
        return num


class Solution: # brute force approach O(n^2)
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            biggest = int(num[i])
            idx = i
            for j in range(i, len(num)):
                if biggest <= int(num[j]):
                    biggest = int(num[j])
                    idx = j
            if biggest != int(num[i]):
                num[i], num[idx] = num[idx], num[i]
                break
        return int(''.join(num))