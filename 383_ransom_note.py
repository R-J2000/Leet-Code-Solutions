# 383 Ransom Note

"""
Solution 1 (most intuitive)

Time Complexity: O(n*m)
Space Complexity: O(1)

Intuition and Approach
- Check to see whether the len of magazine is sufficent to supply the characters needed to construct ransomNote
- Iterate over the characters of ransomNote using counter char. 
- Check if char is in magazine. If yes, remove it from magazine; otherwise, return False

"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
          
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char,"",1)
            else: 
                return False
        return True
