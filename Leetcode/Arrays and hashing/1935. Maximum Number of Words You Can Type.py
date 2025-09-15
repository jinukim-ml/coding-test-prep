class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(list(brokenLetters))
        invalid = 0
        text = text.split()
        for w in text:
            for ch in w:
                if ch in brokenLetters:
                    invalid += 1
                    break
        return len(text) - invalid