class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums)-1
        while l < r:
            left_odd = nums[l]%2
            right_even = nums[r]%2 == 0
            if left_odd and right_even:
                nums[l], nums[r] = nums[r], nums[l]
            elif left_odd:
                r -= 1
            else:
                l += 1
        return nums