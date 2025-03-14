class Solution: # O(n log max(candies))
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def is_possible(num_candies) -> bool:
            max_children = 0
            for pile in candies:
                max_children += pile // num_candies # divde a pile to subpiles and count the subpiles
            return max_children >= k # compare the number of subpiles to k (the number of children)

        l, r = 0, max(candies)
        while l < r:
            mid = (l + r + 1) // 2
            if is_possible(mid):
                l = mid
            else:
                r = mid - 1
        return l