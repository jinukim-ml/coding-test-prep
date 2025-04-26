class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        total = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                total += customers[i]
        window = 0
        l = 0
        res = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            res = max(res, total + window)
        return res