class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = {}
        for n in arr:
            seen[n] = seen.get(n, 0) + 1
        
        for n in seen:
            if 2*n in seen:
                if n != 0:
                    return True
                else:
                    if seen[n] > 1:
                        return True
        return False