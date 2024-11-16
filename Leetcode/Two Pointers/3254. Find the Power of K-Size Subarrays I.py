from collections import deque

class Solution: # Siliding window solution O(N)
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        ans = [-1] * (len(nums) - k + 1)
        dq = deque()

        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            if dq and nums[i] - 1 != nums[i-1]:
                dq.clear()
            dq.append(i)

            if i >= k - 1 and len(dq) == k:
                ans[i-k+1] = nums[dq[-1]]
        return ans

class Solution: # brute force solution O(N^2)
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        ans = []
        for r in range(k-1, len(nums)):
            l = r - k + 1
            for i in range(l+1, r+1):
                if nums[i]-1 != nums[i-1]:
                    ans.append(-1)
                    break
            else:
                ans.append(nums[r])
            l += 1
            r += 1
        return ans