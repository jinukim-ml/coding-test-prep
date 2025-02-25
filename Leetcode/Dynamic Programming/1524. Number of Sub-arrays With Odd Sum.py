class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        offset = 1e9 + 7
        cnt, odd, even, prefix = 0, 0, 1, 0
        for n in arr:
            prefix += n
            if prefix%2:
                odd += 1
                cnt += even
            else:
                even += 1
                cnt += odd
        return int(cnt%offset)