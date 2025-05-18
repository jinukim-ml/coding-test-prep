class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        newarr = []
        for i in range(len(nums)):
            n = nums[i]
            digitsum = 0
            while n:
                n, r = divmod(n, 10)
                digitsum += r
            newarr.append((digitsum, nums[i], i))
        newarr.sort()
        cnt = 0

        positions = [0] * len(nums)
        for i in range(len(nums)):
            og_idx = newarr[i][2]
            positions[og_idx] = i

        vis = [False] * len(nums)
        res = 0
        for i in range(len(nums)):
            if vis[i] or positions[i] == i:
                vis[i] = True
                continue

            cycle_len = 0
            curr = i
            while not vis[curr]:
                vis[curr] = True
                curr = positions[curr]
                cycle_len += 1

            if cycle_len:
                res += cycle_len - 1
        return res