# 125 Valid Palindrome

"""
Solution 1 

Time Complexity: O(n)
Space Complexity:O(1)

Intuition and Approach
- Set two pointers at the start and end of string s
- Iterate over s. Skip over any non-alphanumeric characters
- Compare the alphanumeric characters from the start with those from the end. If one character is not "equal" return False. Otherwise, after all iterations return True.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """         
        left, right = 0, len(s) - 1

        while left < right:         
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1       
        return True
