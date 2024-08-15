class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        register = {5: 0, 10: 0}
        for b in bills:
            if b == 5:
                register[5] += 1
            elif b == 10:
                if register[5]:
                    register[5] -= 1
                    register[10] += 1
                else:
                    return False
            else: # b == 20
                if register[10] and register[5]: # one $5 and one $10
                    register[5] -= 1
                    register[10] -= 1
                elif register[5] >= 3:
                    register[5] -= 3
                else:
                    return False
        return True