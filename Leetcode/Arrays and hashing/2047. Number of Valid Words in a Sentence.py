from collections import defaultdict

class Solution:
    def countValidWords(self, sentence: str) -> int:
        punc = ['!', ',', '.']
        
        res = 0
        sentence = sentence.split()
        for s in sentence:
            indices = defaultdict(list)
            for i, ch in enumerate(s):
                indices[ch].append(i)
            if '-' in indices:
                if len(indices['-']) > 1:
                    continue
                i = indices['-'][0]
                if i == 0 or i == len(s)-1:
                    continue
                if not s[i-1].isalpha() or not s[i+1].isalpha():
                    continue
            for p in punc:
                if p in indices:
                    if len(indices[p]) > 1:
                        break
                    if indices[p][0] != len(s)-1:
                        break
            else:
                for i in range(10):
                    if str(i) in indices:
                        break
                else:
                    res += 1
        return res