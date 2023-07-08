# 80 Remove Duplicates from Sorted Array II

"""
Solution 1 

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach

    TODO 

Special Notes: 
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		# Edge Case
        if len(nums) < 3: 
            return len(nums)
    
		
        tracker = 0  # Pointer from where we need to replace elements
        for i in range(2, len(nums)):
            if nums[i] != nums[tracker]:
                nums[tracker + 2] = nums[i]
                tracker += 1
        return tracker + 2
