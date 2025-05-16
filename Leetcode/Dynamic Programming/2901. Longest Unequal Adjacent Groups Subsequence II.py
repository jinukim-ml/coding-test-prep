from collections import defaultdict

class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        def is_valid(i: int, j: int) -> bool:
            if groups[i] == groups[j]:
                return False
            cnt = 0
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return True
        
        lengths = defaultdict(list)
        dp = [0] * len(words)
        path = [i for i in range(len(words))]
        for i in range(len(words)):
            for j in lengths[len(words[i])]:
                if is_valid(i, j) and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    path[i] = j
            lengths[len(words[i])].append(i)
        max_val, curr = 0, 0
        for i in range(len(dp)):
            if dp[i] > max_val:
                max_val = dp[i]
                curr = i
        res = []
        while curr != path[curr]:
            res.append(words[curr])
            curr = path[curr]
        else:
            res.append(words[path[curr]])
        return res[::-1]