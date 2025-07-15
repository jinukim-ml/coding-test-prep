class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        num_vowels = 0
        num_nums = 0
        for ch in word:
            if not ch.isalnum():
                return False
            else:
                if ch.isnumeric():
                    num_nums += 1
                elif ch.lower() in vowels:
                    num_vowels += 1
        if num_vowels >= 1 and len(word) - num_nums - num_vowels >= 1:
            return True
        else:
            return False