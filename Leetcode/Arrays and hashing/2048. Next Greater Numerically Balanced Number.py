class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for x in range(n+1, 1224445):
            freq = [0 for _ in range(10)]
            val = x
            while val:
                val, r = divmod(val, 10)
                freq[r] += 1
            keys, matches = 0, 0
            for i in range(10):
                if freq[i]:
                    keys += 1
                    if freq[i] == i:
                        matches += 1
                    else:
                        break
            if keys == matches:
                return x