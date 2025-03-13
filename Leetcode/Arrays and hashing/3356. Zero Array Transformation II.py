class Solution: # O(log m * (n + m)), n: length of nums, m: length of queries
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        def is_possible(num_ops: int) -> bool:
            diff = [0] * (len(nums) + 1)
            for i in range(num_ops):
                l, r, v = queries[i]
                diff[l] += v
                diff[r+1] -= v
            
            total_sum = 0
            for i in range(len(nums)):
                total_sum += diff[i]
                if total_sum < nums[i]:
                    return False
            return True
        
        # binary search
        l, r = 0, len(queries)
        if not is_possible(r):
            return -1
        while l <= r:
            mid = (l + r) // 2
            if is_possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

class Solution: # O(n + m) w/ the line sweep algorithm
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        total_sum = 0
        k = 0
        diff = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            while total_sum + diff[i] < nums[i]:
                k += 1
                if k > len(queries):
                    return -1
                
                l, r, v = queries[k-1]
                if r >= i:
                    diff[max(l, i)] += v
                    diff[r+1] -= v
            total_sum += diff[i]
        return k