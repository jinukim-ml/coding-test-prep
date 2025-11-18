class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        while i < len(bits)-2:
            if bits[i] == 1:
                i += 1
            i += 1
        return bits[i] == 0 # if bits[len(bits)-1] == 1, return false