from collections import defaultdict

class Solution: # Two pointers solution. O(n + m)
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                if res and res[-1][0] == nums1[i][0]:
                    res[-1][1] += nums1[i][1]
                else:
                    res.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                if res and res[-1][0] == nums2[j][0]:
                    res[-1][1] += nums2[j][1]
                else:
                    res.append([nums2[j][0], nums2[j][1]])
                j += 1
        while i < len(nums1):
            res.append([nums1[i][0], nums1[i][1]])
            i += 1
        while j < len(nums2):
            res.append([nums2[j][0], nums2[j][1]])
            j += 1
        return res

class Solution: # Brute force solution. O(n + m)
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        book = defaultdict(int)
        for k, v in nums1:
            book[k] += v
        for k, v in nums2:
            book[k] += v
        
        res = []
        for k, v in sorted(book.items()):
            res.append((k, v))
        return res