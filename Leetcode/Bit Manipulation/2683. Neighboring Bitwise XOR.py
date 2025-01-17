class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        xor = 0
        for n in derived:
            xor ^= n
        return True if xor == 0 else False