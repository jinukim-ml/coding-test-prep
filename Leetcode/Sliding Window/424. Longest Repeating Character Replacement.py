class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {}
        left, maxfreq = 0, 0
        for right in range(len(s)):
            table[s[right]] = table.get(s[right], 0) + 1
            
            # No need to find the most frequent element every single time
            # because descreasing maxfreq doesn't affect the result
            # kind of a fancy trick, but this improves performance significantly
            if maxfreq < table[s[right]]: 
                maxfreq = table[s[right]]

            if right - left + 1 - maxfreq > k:
                table[s[left]] -= 1
                left += 1

        return right - left + 1 # We don't need to keep maximum length of the slide window on memory because it never shrinks