from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        table = {char: set() for w in words for char in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    table[w1[j]].add(w2[j])
                    break
        
        vis = {} # True if it's in the current path, False if it's visted but not in the current path
        res = [] # Reverse order

        def dfs(char): # post-order dfs
            if char in vis:
                return vis[char]

            vis[char] = True
            for nei in table[char]:
                if dfs(nei):
                    return True
            vis[char] = False
            res.append(char)

        for char in table:
            if dfs(char):
                return "" # there's a loop. Invalid order
        
        res.reverse()
        return "".join(res)