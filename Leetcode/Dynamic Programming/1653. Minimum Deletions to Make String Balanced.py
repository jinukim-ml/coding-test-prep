class Solution:
    def minimumDeletions(self, s: str) -> int:
        num_a = 0
        for ch in s:
            if ch == 'a':
                num_a += 1
        
        pre_b = 0
        ans = float('inf')
        for ch in s:
            if ch == 'a':
                num_a -= 1
            ans = min(ans, pre_b + num_a)
            if ch == 'b':
                pre_b += 1
        return ans