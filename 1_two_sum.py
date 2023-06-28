# 1 Two Sum

"""
Solution 1 (Nested-For Loops--Brute Force)

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

"""
Solution 2 (Hashmap)

Time Complexity: O(n)
Space Complexity: O(n)

Intuition and Approach
- Exploit that fact that if num1 + num2 == target, then target - num1 = num2
- Initialze a dictionary: int_dict
- Iterate over nums and for each integer determine diff = target - integer. If diff is in int_dict, return the index of both diff and integer
- Otherwise, add integer and its index to int_dict

Special Notes:
Even if you skip over a integer needed to sum to target, as it had not been added to the dictionary, that same integer will emerge as diff in a later iteration
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        int_dict = {}

        for index, integer in enumerate(nums):
            diff = target - integer
            if diff in int_dict:
                return [int_dict[diff], index]
            int_dict[integer] = index
