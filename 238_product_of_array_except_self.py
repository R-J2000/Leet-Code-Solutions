# 238 Product of Array Except Self

"""
Solution 1 

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- The key insight is to calculate the product of all elements to the left of each element and then multiply it by the product 
of all elements to the right of each element. [1, 2, 3, 4, 5] for this array index 2 element 3, the left product will be 1*2 and 
the right product will be 4*5.
- Initialize output array
- Iterate over output, add the left product of each element at their corresponding index. 
- Then iterate over output again (from right to left) and multiply the right product to the previously computed left entries.
- Return output
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n  
        left_product = 1
        right_product = 1
    
        # Calculate the product of all elements to the left of each element
        for i in range(n):
            output[i] *= left_product
            left_product *= nums[i]
    
        # Calculate the product of all elements to the right of each element
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
    
        return output
