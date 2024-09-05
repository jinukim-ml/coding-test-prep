class Solution: # time complexity: O(m+n)
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        s = sum(rolls) # O(m)
        target = mean * (n + len(rolls)) - s

        if n <= target <= 6 * n:
            ans = []
            remaining = n
            for _ in range(n): # O(n)
                for x in range(1, 7):
                    if remaining - 1 <= target - x <= (remaining - 1) * 6:
                        ans.append(x)
                        target -= x
                        remaining -= 1
                        break
            return ans
        else:
            return []