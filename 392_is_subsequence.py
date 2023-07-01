# 392 Is Subsequence

"""
Solution 1 

Time Complexity: O(n)
Space Complexity:O(1)

Intuition and Approach
- Set two pointers that will trace s and t.
- Iterate over t. If the pointers point to the same character, update both pointers. If not, update just the t pointer
- If you iterate "out of s" return True. Otherwise, return False
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_pointer, t_pointer = 0, 0

        if s == "":
            return True

        for t_pointer in range(len(t)):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1

            if s_pointer == len(s):
                return True

        return False
