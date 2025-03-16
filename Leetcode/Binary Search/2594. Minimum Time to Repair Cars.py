from math import ceil

class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def is_possible(expected_time: int) -> bool:
            repaired_cars = 0
            for r in ranks:
                repaired_cars += int((expected_time/r)**0.5)
            return repaired_cars >= cars
        
        l, r = float('inf'), float('-inf')
        for n in ranks:
            l = min(l, n)
            r = max(r, n)
        l *= ceil(cars/len(ranks))
        r *= cars**2
        while l <= r:
            mid = (l + r) // 2
            if is_possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l