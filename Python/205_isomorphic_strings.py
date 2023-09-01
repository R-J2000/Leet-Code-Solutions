# 205 Isomorphic Strings

"""
Solution 1 

Time Complexity: O(n)
Space Complexity:O(n)

Intution and Approach
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


"""
Solution 2 (Bidirectional Mapping Check) 

Time Complexity: O(n)
Space Complexity:O(n)

Intution and Approach
- Create two dictionary with the key-value pairs corresponding to the characters in s and t, In one dictionary the charcters in s and t are the keys and values, respectively. For the second dictionary, characters in t are the key and characters in s will be values
- Iterate over the strings s and t, character by character. 
- If the key-values pairs in BOTH dictionaries are not one-to-one, return False.
- Otherwise, add new entries to the dictionary
- Return True, if the falsehood condition is not met through all iterations

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        st_dict, ts_dict = {}, {}

        for i in range(len(s)):
            char1, char2 = s[i], t[i]

            if ((char1 in st_dict and char2 != st_dict[char1]) or
            (char2 in ts_dict and char1 != ts_dict[char2])):
                return False
            
            st_dict[char1] = char2
            ts_dict[char2] = char1

        
        return True
