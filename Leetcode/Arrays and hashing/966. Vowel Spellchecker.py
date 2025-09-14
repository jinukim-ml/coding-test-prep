class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        exact_matches = set(wordlist)
        lowers, novowels = {}, {}
        def remove_vowels(w: str) -> str:
            res = ''
            vowels = set(['a', 'e', 'i', 'o', 'u'])
            for ch in w:
                if ch in vowels:
                    res += '*'
                else:
                    res += ch
            return res

        for w in wordlist:
            l = w.lower()
            removed = remove_vowels(l)
            if l not in lowers:
                lowers[l] = w
            if removed not in novowels:
                novowels[removed] = w
        res = []
        for q in queries:
            if q in exact_matches:
                res.append(q)
            else:
                l = q.lower()
                removed = remove_vowels(l)
                if l in lowers:
                    res.append(lowers[l])
                elif removed in novowels:
                    res.append(novowels[removed])
                else:
                    res.append("")
        return res