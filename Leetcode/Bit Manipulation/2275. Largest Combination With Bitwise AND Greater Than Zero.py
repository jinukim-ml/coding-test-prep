class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        bit_cnt = [0] * 24
        for i in range(24):
            for n in candidates:
                if n & (1 << i) != 0:
                    bit_cnt[i] += 1
        return max(bit_cnt)