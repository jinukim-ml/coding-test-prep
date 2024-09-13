class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        xor = 0
        for i in range(len(arr)):
            xor ^= arr[i]
            arr[i] = xor
        
        ans = []
        for l, r in queries:
            if l > 0:
                ans.append(arr[l-1] ^ arr[r])
            else:
                ans.append(arr[r])
        return ans