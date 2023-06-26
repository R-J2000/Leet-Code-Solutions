# 26 Remove Duplicates from Sorted Array

"""
Solution 1 (implementation using while loop)
Runtime: 129 ms (beats 16.45%)
Memory: 14.6 MB (beats 64.18%)

Intuition and Approach
- Set a pointer (i). Iterate through the nums array/list. 
- For each iteration compare integer in nums at index [i] with the integer at index [i+1].
- If integer at index [i] equals the integer at index [i-1], pop integer at index [i+1]; otherwise increment i
- Return the post-modification length of nums
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)

"""
Solution 2 (implementation using for loop)
Runtime: 129 ms (beats 16.45%)
Memory: 14.6 MB (beats 64.18%)

Intuition and Approach
- Set a pointer (i). Iterate through the nums array/list. 
- For each iteration compare integer in nums at index [i] with the integer at index [i+1].
- If integer at index [i] equals the integer at index [i-1], pop integer at index [i+1]; otherwise increment i
- Return the post-modification length of nums
"""
