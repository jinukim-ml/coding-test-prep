class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1 = s1.split()
        s2 = s2.split()

        dic1, dic2 = {}, {}
        for k in s1:
            dic1[k] = dic1.setdefault(k, 0) + 1
        for k in s2:
            dic2[k] = dic2.setdefault(k, 0) + 1
        
        ans = []
        for k, v in dic1.items():
            if k not in dic2 and v == 1:
                ans.append(k)
            else:
                if k in dic2:
                    dic2.pop(k)
        
        for k, v in dic2.items():
            if v == 1:
                ans.append(k)
        return ans