class Solution:
    def getLucky(self, s: str, k: int) -> int:
        start = 97
        book = {chr(start + i): str(i + 1) for i in range(26)}

        # convert
        converted = ''
        for ch in s:
            converted += book[ch]
        
        for i in range(k):
            total = 0
            for ch in converted:
                total += int(ch)
            converted = str(total)
        return int(converted)