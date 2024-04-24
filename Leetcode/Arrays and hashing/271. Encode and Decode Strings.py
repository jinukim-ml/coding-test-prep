# There's no emoji in UTF-8 and python supports emoji
from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '👍' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '👍': # end of this j will point thumbs up emoji
                j += 1
            length = int(s[i:j])
            i = j + 1 # start of actual string
            j = i + length # end of the string
            decoded.append(s[i:j])
            i = j
        return decoded