class Solution: # O(n) solution.
    def lexicalOrder(self, n: int) -> list[int]:
        ans = []
        curr = 1
        for _ in range(n):
            ans.append(curr)

            if curr * 10 <= n:
                curr *= 10
            else:
                while curr%10 == 9 or curr >= n:
                    curr //= 10
                curr += 1
        return ans


class Solution: # O(nlogn) solution. Invalid because our algorithm should run in O(n) time.
    def lexicalOrder(self, n: int) -> list[int]:
        return list(map(int, sorted([str(i) for i in range(1,n+1)])))