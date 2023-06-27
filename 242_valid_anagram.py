# 242 Valid Anagram

"""
Solution 1 (Sort)

Time Complexity: O(nlogn)
Space Complexity: O(1)

Intuition and Approach
- Sort both anagram and compare. If they are the same, return True; otherwise, return false.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True     
        return False
