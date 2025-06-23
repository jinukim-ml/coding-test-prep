class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            for l in range(len(s)//2):
                r = len(s)-l-1
                if s[l] != s[r]:
                    return False
            return True

        res = 0
        length = 1
        while n:
            half_len = (length+1)//2
            start_root = k**(half_len-1)
            end_root = k**half_len
            for root_val in range(start_root, end_root):
                s_root = ''
                temp = root_val
                while temp:
                    s_root = str(temp%k) + s_root
                    temp //= k
            
                if length%2:
                    pal = s_root + s_root[:-1][::-1]
                else:
                    pal = s_root + s_root[::-1]
                b10 = int(pal,k)
                if is_palindrome(str(b10)):
                    n -= 1
                    res += b10
                    if n == 0:
                        return res
            
            length += 1
        return res