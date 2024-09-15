class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans = 0
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        curr = 0
        first_seen = [-1] * 32
        first_seen[0] = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                curr ^= vowels[ch]
            
            if first_seen[curr] == -1:
                first_seen[curr] = i + 1
            
            ans = max(ans, i + 1 - first_seen[curr])
        return ans