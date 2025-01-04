class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = [0] * 26
        for ch in s:
            right[ord(ch) - 97] += 1
        
        left = [0] * 26
        combinations = set()
        for ch in s:
            i = ord(ch) - 97
            right[i] -= 1
            for j in range(26):
                if left[j] > 0 and right[j] > 0:
                    outside = chr(j + 97)
                    combinations.add(outside + ch)
            left[i] += 1
        return len(combinations)