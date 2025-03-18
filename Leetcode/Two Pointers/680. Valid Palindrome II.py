class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_possible(l: int, r: int, cnt: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    cnt += 1
                    if cnt > 1:
                        return False
                    else:
                        if is_possible(l+1, r, cnt):
                            return True
                        elif is_possible(l, r-1, cnt):
                            return True
                        else:
                            return False
                l += 1
                r -= 1
            return True
        return is_possible(0, len(s)-1, 0)