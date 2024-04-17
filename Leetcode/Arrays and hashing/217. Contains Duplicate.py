class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        if len(s) < len(nums):
            return True
        else:
            return False