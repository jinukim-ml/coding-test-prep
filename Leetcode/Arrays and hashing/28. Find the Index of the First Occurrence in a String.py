class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, p2 = 0, 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i] == needle[0]:
                p1 = i
                while p1 < len(haystack) and p2 < len(needle) and haystack[p1] == needle[p2]:
                    p1 += 1
                    p2 += 1
                if p2 == len(needle):
                    return i
                else:
                    p2 = 0
            i += 1
        return -1