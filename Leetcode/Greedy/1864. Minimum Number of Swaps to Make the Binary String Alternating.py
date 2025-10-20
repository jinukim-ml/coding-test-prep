class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones
        if abs(ones - zeros) > 1:
            return -1

        def get_swaps(x: str):
            cnt = 0
            for ch in s:
                if ch != x:
                    cnt += 1
                if x == '0':
                    x = '1'
                else:
                    x = '0'
            return cnt//2
        
        if ones > zeros:
            return get_swaps('1')
        elif ones < zeros:
            return get_swaps('0')
        else:
            return min(get_swaps('0'), get_swaps('1'))