# 202 Happy Number

"""
Solution 1 (Recursive Approach)

Time Complexity: ?
Space Complexity: ?

Intuition and Approach
- Initialize a variable (seen )that keeps track of all the arguments passed into the recursive call
- Design a helper function that checks whether the previous sum == 1 and whether it has been encountered. In the first scenario return True and False in the second.
- If neither conditions are satisfied add the previous sum to the seen set.
- Do the happy number computation for the prev_sum. Pass the new sum to the helper function, recursively
- Return the result of helper(n)

"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()
        prev_sum = n

        def helper(prev_sum):
            if prev_sum == 1: 
                return True
            if prev_sum in seen:
                return False
            seen.add(prev_sum)

            next_sum = 0

            for integer in str(prev_sum):
                next_sum += int(integer)**2
            return helper(next_sum)
        
        return helper(n)
