class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        
        locked_left = []
        unlocked = []
        for i, ch in enumerate(s):
            if locked[i] == '0':
                unlocked.append(i)
            elif ch == '(':
                locked_left.append(i)
            else:
                if locked_left:
                    locked_left.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        
        while locked_left and unlocked and locked_left[-1] < unlocked[-1]:
            locked_left.pop()
            unlocked.pop()
        
        if locked_left:
            return False
        else:
            return True