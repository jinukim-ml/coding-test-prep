class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        ptr = 0
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]
        return slow