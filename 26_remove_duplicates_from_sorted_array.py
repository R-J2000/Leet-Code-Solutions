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
Solution 2 (for loop + two pointers in use)
Runtime: 50 ms (beats 99.90%)
Memory: 15 MB (beats 8.12%)

Intuition and Approach
- Set two pointers i and j. j will keep track the number of unique elements encountered thus far and i will trace the list/array in range(1, len(nums))
- j will point to the first instance of a unique element. i will continuing looping until it finds the very next unique element
- The next unique element, once found, will be placed following the last unique element.
- j will point to the newly situated/displaced unique element.
- This process of updating and incrementing will continue until i has reached the last element and j is pointing to the final unique element (alternatively, 
when j is pointing to the largest unique element in the list).
"""

class Solution(object):
	def removeDuplicates(self, nums):
		j = 0
		for i in range(1, len(nums)):
			if nums[j] != nums[i]:
				j += 1
				nums[j] = nums[i]
		return j + 1
