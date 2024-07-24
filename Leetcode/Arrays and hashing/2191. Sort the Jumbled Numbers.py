class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        book = {}
        for i, destination in enumerate(mapping):
            book[str(i)] = str(destination)

        ans, origins = [], {}
        for i, num in enumerate(nums):
            origins[i] = num
            converted = ''
            for digit in str(num):
                converted += book[digit]
            ans.append((int(converted), i))
        
        ans.sort()
        for i in range(len(ans)):
            converted, og_idx = ans[i]
            ans[i] = origins[og_idx]
        return ans