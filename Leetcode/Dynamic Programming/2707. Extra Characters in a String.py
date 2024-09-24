# Bottom-up DP
class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dp = [0] * (len(s) + 1)
        dictionary = set(dictionary)

        for i in range(len(s)-1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr in dictionary:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]

# Trie + bottom-up DP
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dp = [0] * (len(s) + 1)
        root = Trie(dictionary).root

        for i in range(len(s)-1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            curr = root
            for j in range(i, len(s)): # slicing is replaced (faster execution)
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]

# Trie + Top-down DP (memoization)
class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dp = {len(s): 0}
        root = Trie(dictionary).root
        
        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1)
            curr = root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res
        return dfs(0)