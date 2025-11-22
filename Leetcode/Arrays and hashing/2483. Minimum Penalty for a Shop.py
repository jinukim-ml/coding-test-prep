class Solution:
    def bestClosingTime(self, customers: str) -> int:
        missed = 0
        hrs_empty = customers.count('N')
        min_pen, res = hrs_empty, len(customers)
        for i in reversed(range(len(customers))):
            if customers[i] == 'Y':
                missed += 1
            else:
                hrs_empty -= 1
            penalty = hrs_empty + missed
            if penalty <= min_pen:
                min_pen = penalty
                res = i
        return res