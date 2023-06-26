
"""
Solution 1 
Runtime: 141 ms (beats 54.48%)
Memory: 14.9 MB (beats 86.61%)

Intuition and Approach
- Initialize a dictionary (counter_dict) and use for loop to traverse nums using the pointer i
- Add each new instance of an element as a key in counter_dict, with 1 as its corresponding value
- Otherwise, if the current element is already in counter_dict, increment its value by 1
- Check if the majority value condition is satisfied for i. If so, return i
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter_dict = {}
        majority_val = floor(len(nums)/2) + 1
        for i in nums:
            if i not in counter_dict:
                counter_dict[i] = 1
            else:
                counter_dict[i] += 1
                if counter_dict[i] == majority_val:
                    return i
        return i
