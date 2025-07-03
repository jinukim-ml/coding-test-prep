from math import ceil, log

class Solution: # simulation
    def kthCharacter(self, k: int) -> str:
        num_ops = ceil(log(k,2))
        word = ['a']
        for _ in range(num_ops):
            length = len(word)
            for i in range(length):
                ch = chr((ord(word[i])+1-97)%26 + 97)
                word.append(ch)
        return word[k-1]

class Solution: # bit manipulation
    def kthCharacter(self, k: int) -> str:
        return chr(97 + (k-1).bit_count())