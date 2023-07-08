# 189 Rotate Array

"""
Solution 1

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Define helper function that allows you to reverse a sub-array from defined indicies
- Update k to minimize the number of rotations. A k value of 11 and 21 for an array of length 10, will have the same 
end result. Do this by exploiting the modulus operator
- Reverse nums
- Reverse the first k element of nums 
- Reverse the last len(nums) - k of nums
"""
class Solution(object):         
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n  
        
        reverse(nums, 0, n - 1)  
        reverse(nums, 0, k - 1)  
        reverse(nums, k, n - 1)
