"""
Solution 1

Runtime: 31 ms (beats 88.55%)
Memory: 13.4 MB (beats 67.61)

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Set up a dictionary with the key-value pairs corresponding to the roman-integer pairs
- Make replacements in s to account for the exceptions in the roman system
- Iterate over the roman numerial represented as a string and add the appropriate value to a total sum
"""

class Solution(object):
    def romanToInt(self, s):
	roman_dict = {
		'I' : 1,
		'V' : 5,
		'X' : 10,
		'L' : 50,
		'C' : 100,
		'D' : 500,
		'M' : 1000
	}

	s = s.replace("IV", "IIII").replace("IX", "IIIIIIIII")
	s = s.replace("XL", "XXXX").replace("XC", "XXXXXXXXX")
	s = s.replace("CD", "CCCC").replace("CM", "CCCCCCCCC")

	sum = 0
	for key in s:
		sum += roman_dict[key]

	return sum
