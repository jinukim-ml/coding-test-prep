class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prefix = ""
        pos = 0
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break
        return prefix