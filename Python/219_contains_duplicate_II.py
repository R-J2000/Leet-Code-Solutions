# 219 Contains Duplicate II

"""
Solution 1 (Sliding Window Approach)

Time Complexity: O(n)
Space Complexity: O(n)

Intuition and Approach
- Initialize a "window" delineated by two points: left and right
- Iterate over the length of nums
- During each iteration, check whether duplicates emerge in the window of a max size k. Update the left and right 
pointers to "keep the window sliding." Add or remove the elements in the window set appropriately

"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Initialize HashSet
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            
            if nums[right] in window:
                return True

            window.add(nums[right])
        
        return False
