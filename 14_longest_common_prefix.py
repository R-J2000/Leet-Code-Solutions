# 14 Longest Common Prefix

"""
Solution 1

Time Complexity: O(nlog(n))
Space Complexity: O(1)

Intuition and Approach
- Sort strs in alphabetical order
- Select the first and the last string
- Determine the longest common prefix for the first and the last string in the sorted strs and return it
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        long_pre = []
 
        if strs and len(strs) > 0:
            strs = sorted(strs) 
            first, last = strs[0], strs[-1] 
            for i in range(len(first)):
                if len(last) > i and last[i] == first[i]:
                    long_pre.append(last[i])
                else:
                    return "".join(long_pre)
        return "".join(long_pre)

"""
Solution 2

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Iterate over the range of the first string (or any random string)
- For each string in strs, compare there ith characters to the ith character of the first string
- Update the variable long_pre every time the ith element of ALL the elements in the string are found to be the same 
- If a discrepancy is found, return long_pre

Special Notes:
- To avoid going out-of-bounds during the character comparison, ensure that the current character to be assessed (denoted by i) does not fall beyond the last character of ANY character. If this were to occur we would have come across the smallest string in strs with a length i-1. Return long_pre at this point.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        long_pre = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return long_pre
            long_pre += strs[0][i]
        return long_pre
