import heapq

class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        arr = [(nums1[i], nums2[i], i) for i in range(len(nums1))]
        arr.sort(key=lambda x: x[0])

        res = [0] * len(nums1)
        running_sum = 0
        i = 0
        h = []
        while i < len(nums1):
            j = i
            while j < len(nums1) and arr[i][0] == arr[j][0]:
                og_idx = arr[j][2]
                res[og_idx] = running_sum
                j += 1

            for idx in range(i, j):
                val = arr[idx][1]
                if len(h) < k:
                    heapq.heappush(h, val)
                    running_sum += val
                elif val > h[0]:
                    removed = heapq.heapreplace(h, val)
                    running_sum += val - removed
            i = j
        return res