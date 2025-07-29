from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l, res = 0, 0
        basket = defaultdict(lambda: 0)
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
            res = max(res, r-l+1)
        return res