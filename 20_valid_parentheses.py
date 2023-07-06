# 20 Valid Parentheses

"""
Solution 1 

Time Complexity: O(n)
Space Complexity: O(n)

Intuition and Approach
- Iterate over s. 
- If you come across left bracket, append to stack
- If you come across right bracket, compare it to the "topmost" element or latest addition to the stack.
- If they do not match--return false, otherwise continue with iterations
- Finally, return True if stack is empty at the end of the iteration. Otherwise, return False 

Special Notes: 
You need to check for the condition len(stack) == 0, to ensure you are not trying to pop off an empty stack
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_dict = {'(':')',
                        '{':'}',
                        '[':']'}

        for bracket in s:
            if bracket in bracket_dict:
                stack.append(bracket)
            elif len(stack) == 0 or bracket_dict[stack.pop()] != bracket:
                return False
        
        return len(stack) == 0
