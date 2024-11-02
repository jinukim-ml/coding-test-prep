class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        for i in range(1, len(sentence)):
            prev, curr = sentence[i-1], sentence[i]
            if prev[-1] != curr[0]:
                return False
        if sentence[-1][-1] != sentence[0][0]:
            return False
        return True