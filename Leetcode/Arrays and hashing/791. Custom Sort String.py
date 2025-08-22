class Solution: # O(n log n)
    def customSortString(self, order: str, s: str) -> str:
        priorities = [float('inf') for _ in range(26)]
        for i, ch in enumerate(order):
            priorities[ord(ch)-97] = i
        s = [[ch, priorities[ord(ch)-97]] for ch in s]
        s.sort(key=lambda x: x[1])
        res = ''
        for ch, _ in s:
            res += ch
        return res

class Solution: # O(n)
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = ''
        for ch in order:
            if ch in freq:
                res += ch * freq.pop(ch)
        for ch in freq:
            res += ch * freq[ch]
        return res
