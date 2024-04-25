from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Generate all possible substrings
        candidates = []
        string = ""
        
        for i in range(len(s)):
            string = s[i]
            candidates.append(string)
            for j in range(i+1, len(s)):
                string += s[j]
                candidates.append(string)

        print(candidates)
        maxstreak = 0
        for c in candidates:
            if len(c) == len(set(c)) and len(c) > maxstreak:
                maxstreak = len(c)
        
        return maxstreak