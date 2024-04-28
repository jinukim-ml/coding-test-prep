class Solution: # Original solution. O(mn)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        t1, t2 = {}, {}
        
        for i in range(n1):
            t1[s1[i]] = t1.get(s1[i], 0) + 1
            t2[s2[i]] = t2.get(s2[i], 0) + 1
        
        matches = 0
        for k, v in t1.items():
            if k in t2 and v == t2[k]:
                matches += 1
                
        if matches == len(t1):
            return True
        
        l = 0
        for r in range(n1, n2):
            t2[s2[r]] = t2.get(s2[r], 0) + 1
            t2[s2[l]] -= 1
            l += 1

            matches = 0
            for k, v in t1.items():
                if k in t2 and v == t2[k]:
                    matches += 1
            if matches == len(t1):
                return True
        return False

class Solution: # More polished solution. O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        count1, count2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i])-97] += 1
            count2[ord(s2[i])-97] += 1
        
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        l = 0
        for r in range(n1, n2):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - 97
            count2[idx] += 1 # move the right pointer of our sliding window to the right
            if count1[idx] == count2[idx]:
                matches += 1
            elif count1[idx] + 1 == count2[idx]:
                matches -= 1

            idx = ord(s2[l]) - 97
            count2[idx] -= 1
            if count1[idx] == count2[idx]:
                matches += 1
            elif count1[idx] - 1 == count2[idx]:
                matches -= 1
            l += 1

        return matches == 26