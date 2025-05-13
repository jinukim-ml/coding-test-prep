class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        characters = [0] * 26
        for ch in s:
            characters[ord(ch)-97] += 1
        for i in range(t):
            offset = characters[-1]
            characters[-1] = 0
            for j in range(24, -1, -1):
                characters[j+1] = characters[j]
                characters[j] = 0
            characters[0] += offset
            characters[1] += offset
        res = 0
        for n in characters:
            res += n
        return res%(10**9 + 7)