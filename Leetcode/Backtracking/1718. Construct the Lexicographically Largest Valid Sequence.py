class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        length = 2*n - 1
        res = [0] * length
        indices = [False] * (n + 1)
        def backtrack(i: int) -> bool:
            if i == length:
                return True
            if res[i] != 0:
                if backtrack(i+1):
                    return True
                else:
                    return False
            for x in range(n, 0, -1):
                if not indices[x]:
                    if x != 1:
                        if i+x < length and res[i+x] == 0:
                            res[i] = x
                            res[i+x] = x
                            indices[x] = True
                            if backtrack(i+1):
                                return True
                            res[i] = 0
                            res[i+x] = 0
                            indices[x] = False
                    else: # x == 1
                        res[i] = x
                        indices[x] = True
                        if backtrack(i+1):
                            return True
                        res[i] = 0
                        indices[x] = False
            return False
        
        backtrack(0)
        return res