class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        i = 0
        while i < min(len(version1), len(version2)):
            a, b = int(version1[i]), int(version2[i])
            if a > b:
                return 1
            elif a < b:
                return -1
            i += 1
        
        if len(version1) >= len(version2):
            for j in range(i, len(version1)):
                if int(version1[j]):
                    return 1
        else:
            for j in range(i, len(version2)):
                if int(version2[j]):
                    return -1
        return 0