class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        l = 0
        while l < len(word):
            cnt, r = 0, l
            while r < len(word) and cnt < 9 and word[l] == word[r]:
                cnt += 1
                r += 1
            comp += str(cnt) + word[l]
            l = r
        return comp