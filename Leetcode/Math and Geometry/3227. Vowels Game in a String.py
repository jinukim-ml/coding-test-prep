class Solution: # O (n)
    def doesAliceWin(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for ch in s:
            if ch in vowels:
                return True
        return False

class Solution: # Simulation. O(n)
    def doesAliceWin(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        def alice(start: int) -> int:
            num_vowels = 0
            last_index = -1
            for r in range(start, len(s)):
                if s[r] in vowels:
                    num_vowels += 1
                    if num_vowels % 2:
                        last_index = r
            return last_index
            
        def bob(start: int) -> int:
            num_vowels = 0
            last_index = -1
            for r in range(start, len(s)):
                if s[r] in vowels:
                    num_vowels += 1
                    if num_vowels % 2 == 0:
                        last_index = r
            return last_index
        
        turn = 1
        idx = 0
        while True:
            if turn == 1:
                idx = alice(idx)
                if idx == -1:
                    return False
            else:
                idx = bob(idx)
                if idx == -1:
                    return True
            turn *= -1