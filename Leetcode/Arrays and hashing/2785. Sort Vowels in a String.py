class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        arr = []
        for ch in s:
            if ch in vowels:
                arr.append(ch)
        arr.sort()
        i = 0
        s = list(s)
        for j, ch in enumerate(s):
            if ch in vowels:
                s[j] = arr[i]
                i += 1
        return ''.join(s)