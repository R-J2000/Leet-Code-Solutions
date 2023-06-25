# 27 Remove Element

"""
Key Insights
1. Simply overwrite the values in the nums array with the desired values

"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
