# 80 Remove Duplicates from Sorted Array II

"""
Solution 1 

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Account of the edge case were nums only has 2 or fewer elements
- Initialize tracker variable
- Interate nums from index 2 onwards. 
- Any time nums[tracker] != nums[i], (i.e we come across a non-duplicate entry) modify the list, 
by overwriting the value at the index tracker with the non-duplicate value. Increment tracker by 1.
- In the end, return tracker

Special Notes: 
Realize that anytime nums[i] == nums[tracker] implies a value with more than 2 duplicates. tracker can be used to keep track of this position. Once we come across
a distinct value, the overwriting process can begin.
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
    
		
        tracker = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[tracker - 2]:
                nums[tracker] = nums[i]
                tracker += 1
        return tracker
