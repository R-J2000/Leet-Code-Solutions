# 58 Length of Last Word
"""
Solution 1 

Time Complextiy: O(n)
Space Complexity: O(1)

Intuition and Approach
- Begin Iteration at the end of the array s
- Decrement pointer if we encounter a space (at the end of the string)
- Start incrementing the variable length when a non-space character is encountered. 
- Return length when another space character is encountered
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
