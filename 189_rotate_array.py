# 189 Rotate Array

"""
Solution 1

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Define helper function that allows you to reverse a sub-array from defined indicies
- Update k to minimize the number of rotations. A k value of 11 and 21 for an array of length 10, will have the same 
end result. Do this by exploiting the modulus operator
- Reverse the first len(nums) - k of nums
- Reverse the last k element of nums
- Reverse nums
"""
class Solution(object):
    def reverse (self, nums, left_ind, right_ind) : 

        while left_ind < right_ind:
            temp = nums[left_ind]
            nums[left_ind] = nums[right_ind]
            nums[right_ind] = temp
            
            left_ind += 1
            right_ind -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);
