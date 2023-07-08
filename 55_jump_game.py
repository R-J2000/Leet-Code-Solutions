# 55 Jump Game

"""
Solution 1 

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Our goal is to reach the last element of nums. Initialize a variable goal to the last index.
- Interate through nums from right to left (back to front). 
- If we can "jump" from index i to goal, we reset goal = i. The intution being that getting to i will ensure that we can get to the last index, hence 
it can be our new goal
- If goal == 0, then return True. This means their is a path from index 0 to the last index. Otherwise, return false.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return True if goal == 0 else False
