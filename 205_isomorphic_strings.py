# 205 Isomorphic Strings

"""
Solution 1 

Time Complexity: O(n)
Space Complexity:O(n)

Inution and Approach
- Create a dictionary with the key-value pairs corresponding to the characters in s and t
- Iterate over the strings s and t, character by character. 
- Add new entries to the dictionary if certain characters are not in dictionary
- For recurring charcters check to see if the values match preexiting entries in the dictionary. If they don't return false.
- Return True, if the condition of falsehood is not met

"""



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        iso_dict = {}

        for i in range(len(s)):
            if s[i] not in iso_dict and t[i] not in iso_dict.values():
                iso_dict[s[i]] = t[i]
            elif t[i] != iso_dict.get(s[i]):
                return False
        
        return True
