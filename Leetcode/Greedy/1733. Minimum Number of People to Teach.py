from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        langs = defaultdict(set)
        for i, available in enumerate(languages, start=1):
            for l in available:
                langs[i].add(l)

        need_language = set()
        for u, v in friendships:
            communicable = False
            for l in langs[u]:
                if l in langs[v]:
                    communicable = True
                    break
            if not communicable:
                need_language.add(u)
                need_language.add(v)
        
        res = float('inf')
        for l in range(1, n+1):
            cnt = 0
            for node in need_language:
                if l not in langs[node]:
                    cnt += 1
            res = min(res, cnt)
        return res