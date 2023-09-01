# 26 Remove Duplicates from Sorted Array

"""
Solution 1 (implementation using while loop)

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
Solution 2 (for loop + two pointers in use)

Intuition and Approach
- Set two pointers left (for left pointer) and right (for right pointer). left will keep track the number of unique elements encountered 
thus far and right will trace the list/array in range(1, len(nums))
- left will point to the first instance of a unique element. right will continuing looping until it finds the very next unique element
- The next unique element, once found, will be placed following the last unique element.
- left will point to the newly situated/displaced unique element.
- This process of updating and incrementing will continue until right has reached the last element and left is pointing to the final unique element (alternatively, 
when left is pointing to the largest unique element in the list).
"""

class Solution(object):
	def removeDuplicates(self, nums):
		left = 0
		for right in range(1, len(nums)):
			if nums[left] != nums[right]:
				left += 1
				nums[left] = nums[right]
		return left + 1
