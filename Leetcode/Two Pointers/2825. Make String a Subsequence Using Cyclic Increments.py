class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        arr = [chr(97 + i) for i in range(26)]
        j = 0
        for i in range(len(str1)):
            if j < len(str2) and (str1[i] == str2[j] or arr[((ord(str1[i]) - 97)+1)%26] == str2[j]):
                j += 1
        
        return j == len(str2)