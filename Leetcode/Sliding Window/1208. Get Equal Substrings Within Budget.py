class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxlen = 0
        l, cur_cost = 0, 0

        for r in range(len(s)):
            cur_cost += abs(ord(s[r]) - ord(t[r]))

            if cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            else:
                maxlen = max(maxlen, r - l + 1)
        return maxlen