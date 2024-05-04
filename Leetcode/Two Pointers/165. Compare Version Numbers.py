class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        comp = 0
        shortest = min(len(v1), len(v2))
        i = 0
        while i < shortest:
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        
        if len(v1) > len(v2):
            for j in range(i, len(v1)):
                if v1[j] > 0:
                    comp += 1
        elif len(v1) < len(v2):
            for j in range(i, len(v2)):
                if v2[j] > 0:
                    comp -=1

        if comp > 0:
            return 1
        elif comp < 0:
            return - 1
        else:
            return 0