class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i+97): None for i in range(26)}
        
        def find(i: str) -> str:
            if not parent[i]:
                parent[i] = i
                return i
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(u: str, v: str) -> None:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                if root_u < root_v:
                    parent[root_v] = root_u
                else:
                    parent[root_u] = root_v
        
        n = len(s1)
        for i in range(n):
            union(s1[i], s2[i])
        for i in range(26):
            find(chr(i+97))

        res = ''
        for ch in baseStr:
            res += parent[ch]
        return res
