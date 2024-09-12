class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        unique = set()
        for ch in allowed:
            unique.add(ch)
        
        ans = 0
        for w in words:
            cnt = 0
            for ch in w:
                if ch in unique:
                    cnt += 1
                else:
                    break
            if cnt == len(w):
                ans += 1
                print(f'w: {w}')
        return ans