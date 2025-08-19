class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        tolerance = 1e-6
        def backtrack(pool: list[float]) -> bool:
            if len(pool) == 1:
                return abs(pool[0]-24) < tolerance
            for i in range(len(pool)):
                for j in range(len(pool)):
                    if i == j:
                        continue
                    new_pool = [pool[k] for k in range(len(pool)) if k != i and k != j]
                    if backtrack(new_pool + [pool[i]+pool[j]]):
                        return True
                    if backtrack(new_pool + [pool[i]-pool[j]]):
                        return True
                    if backtrack(new_pool + [pool[i]*pool[j]]):
                        return True
                    if pool[j] != 0 and backtrack(new_pool + [pool[i]/pool[j]]):
                        return True
            return False
        return backtrack(cards)
