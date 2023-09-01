# 28. Find the Index of the First Occurrence in a String

"""
Solution 1 (Sliding Window Approach)

Time Complexity: O(n*m)
Space Complexity: O(1)

Intuition and Approach
1. Use a nested for loop. The outer loop (h-pointer) will sift through the potential starting index
2. Use the inner loop to compare the charcters of the haystack against those in needle, iteratively. 
3. If all characters match (n-pointer == len(needle) - 1), return the h-pointer. Otherwise, return -1.

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for h_pointer in range(len(haystack) + 1 - len(needle)):
            for n_pointer in range(len(needle)):
                if haystack[h_pointer + n_pointer] != needle[n_pointer]:
                    break
                elif n_pointer == len(needle) - 1:
                    return h_pointer
        return -1
