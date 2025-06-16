class Solution:
    def generateTag(self, caption: str) -> str:
        res = '#'
        capitalize = False
        for ch in caption:
            if len(res) == 100:
                break
            if ch == ' ':
                capitalize = True if len(res) > 1 else False
            else:
                if capitalize:
                    res += ch.upper()
                    capitalize = False
                else:
                    res += ch.lower()
        return res