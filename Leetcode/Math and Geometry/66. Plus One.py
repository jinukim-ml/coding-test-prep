from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry, res = divmod(digits[i] + carry, 10)
            digits[i] = res
            if not carry:
                break
            else:
                if i == 0:
                    digits = [1] + digits
        return digits