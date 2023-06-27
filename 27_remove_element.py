# 27 Remove Element

"""
Solution 1

Intuition and Approach
- Iterate over nums.
- Overwrite the elements need to be removed. Implicity we are usign two pointer: i and x
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
