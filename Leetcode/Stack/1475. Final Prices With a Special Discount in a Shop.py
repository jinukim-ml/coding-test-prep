class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        rev = []
        for i in range(len(prices)-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                rev.append(prices[i] - stack[-1])
            else:
                rev.append(prices[i])
            stack.append(prices[i])
        return rev[::-1]