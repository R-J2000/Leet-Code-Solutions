# 1 Two Sum

"""
Solution 1 (Nested-For Loops)

Time Complexity: O(n^2)
Space Complexity: O(1)

Intuition and Approach
- Use a nested For-Loop and two pointers
- For each int in nums, compute its sum with every other int (except itself) to see if it equal the target
- Return the index of the int values in nums that sum to target

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for first_int in range(len(nums)):
            for second_int in range(len(nums)):
                if nums[first_int] + nums[second_int] == target and first_int != second_int:
                    return [first_int, second_int]
