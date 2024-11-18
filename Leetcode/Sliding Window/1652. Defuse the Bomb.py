class Solution: # O(N)
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        ans = []
        if k > 0:
            l = 1 % n
            r = l
            window = 0
            for _ in range(k):
                window += code[r]
                r = (r + 1) % n
            r = (l + k - 1) % n
            for _ in range(n):
                ans.append(window)
                window -= code[l]
                l = (l + 1) % n
                r = (r + 1) % n
                window += code[r]
        else:
            l = n + k
            r = l
            window = 0
            for _ in range(-k):
                window += code[r]
                r = (r + 1) % n
            r = (l - k - 1) % n
            for _ in range(n):
                ans.append(window)
                window -= code[l]
                l = (l + 1) % n
                r = (r + 1) % n
                window += code[r]
        return ans

class Solution: # brute force O(N^2)
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        ans = []
        if k > 0:
            for i in range(n):
                j = (i+1)%n
                next_sum = 0
                for _ in range(k):
                    next_sum += code[j]
                    j = (j+1)%n
                ans.append(next_sum)
        else:
            k *= -1
            for i in range(n):
                j = (i-1)%n
                prev_sum = 0
                for _ in range(k):
                    prev_sum += code[j]
                    j = (j-1)%n
                ans.append(prev_sum)
        return ans