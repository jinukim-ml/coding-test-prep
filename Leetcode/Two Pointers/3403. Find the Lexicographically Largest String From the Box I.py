class Solution: # O(n^2)
    def answerString(self, word: str, numFriends: int) -> str: 
        if numFriends == 1:
            return word
        
        size = len(word) - numFriends + 1
        res = ''
        for i in range(len(word)):
            w = word[i:min(i+size, len(word))]
            res = max(res, w)
        return res

class Solution: # O(n) two pointer
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        i, j = 0, 1
        while j < n:
            k = 0
            while j + k < n and word[i+k] == word[j+k]:
                k += 1
            if j + k < n and word[i+k] < word[j+k]:
                i, j = j, max(j+1, i+k+1)
            else:
                j += k+1
        return word[i:min(n, i + n - numFriends + 1)]