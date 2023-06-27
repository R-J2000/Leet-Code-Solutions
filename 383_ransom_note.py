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

"""
Solution 2 (Two Dictionaries)

Time Complexity: O(n*m)
Space Complexity: O(n+m)

Intuition and Approach
- Check to see whether the len of magazine is sufficent to supply the characters needed to construct ransomNote
- Generate two dictionaries for each ransomNote and magazine. Store each unique character and its number of occurences as key-value pairs, respectively
- Iterate over the characters of ransomNote using counter char. 
- If char is NOT in the magazine dictionary or the value of char in magazinze dictionary is lower than that in the ransom dictionary, return False. Otherwise, 
return True

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
        
        ransom_dict = {}
        mag_dict = {}

        for ransom_char in ransomNote:
            if ransom_char not in ransom_dict:
                ransom_dict[ransom_char] = 1
            else:
                ransom_dict[ransom_char] += 1
        
        for mag_char in magazine:
            if mag_char not in mag_dict:
                mag_dict[mag_char] = 1
            else:
                mag_dict[mag_char] += 1

        for char in ransomNote:
            if char not in mag_dict or mag_dict[char] < ransom_dict[char]:
                return False
        
        return True
