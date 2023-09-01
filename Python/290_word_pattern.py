# 290 Word Pattern

"""
Solution 1 (Bidirectional Mapping) 

Time Complexity: O(n)
Space Complexity:O(n)

Intuition and Approach
- Create two dictionary with the key-value pairs corresponding to the characters in pattern and words in s. In one dictionary the characters in pattern and words in s
are the keys and values, respectively. For the second dictionary, words in s are the key and characters in pattern will be values
- Iterate over pattern and each word in s, element by element. This can be done by convert s to a list of words in s.
- Check if the length of pattern and words_list is the same. If not, return False.
- If the key-values pairs in BOTH dictionaries are not one-to-one, return False.
- Otherwise, add new entries to the dictionary and loop to completion
- Return True, if none of the falsifying conditions are not met

"""
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        pattern_to_word_map, word_to_pattern_map = {}, {}

        for i in range(len(pattern)):
            char = pattern[i]
            words_list = s.split()
            word = words_list[i]

            if len(pattern) != len(words_list):
                return False

            if ((char in pattern_to_word_map and word != pattern_to_word_map[char]) or
            (word in word_to_pattern_map and char != word_to_pattern_map[word])):
                return False
            
            pattern_to_word_map[char] = word
            word_to_pattern_map[word] = char

        
        return True

      
