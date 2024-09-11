class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        ans = 0
        l = 0
        total = 0
        for r in range(k):
            total += arr[r]
        
        avg = total / k
        if avg >= threshold:
            ans += 1
        
        for r in range(k, len(arr)):
            total -= arr[l]
            l += 1
            total += arr[r]
            avg = total / k
            if avg >= threshold:
                ans += 1
        return ans