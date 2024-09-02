class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        prefixsum = 0
        for c in chalk:
            prefixsum += c
            if prefixsum > k:
                break

        k %= prefixsum
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            else:
                k -= chalk[i]
        return 0