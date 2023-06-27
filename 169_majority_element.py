# 169 Majority Element
"""
Solution 1 

Time Complextiy: O(n)
Space Complexity: O(n)

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

"""
Solution 2 (One-Line Solution)

Runtime: 135 ms (beats 80.47%)
Memory: 14.5 MB (beats 97.8%)

Time Complexity: O(nlog(n)) (as we must sort the array first)
Space Complexity: Depends on the sorting algorithim used

Intuition and Approach
- Sort nums. Return the middle element. 
- Since the majority of elements always exist in the array, the middle element of the sorted array will be the majority element
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]

"""
[Best] Solution 3 (Boyer Moore Algorithim)

Runtime:
Memory:

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Set two counter res and count. res will track element value and count will be responsible for the element count
- Iterate through nums. 
- If count is 0, udpate res to n. 
- Increment count if n == res, otherwise decrement count

In this approach, res is always the majority element of the set of element traversed so far. (Given that the array is guranteed to have a majority element).
The majority element is bound to rack up more increments than decrements; hence the final res value will always belong to it.

"""

class Solution(object):
    def majorityElement(self, nums):
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            # Increment count if n == res, otherwise decrement count
            count += (1 if n == res else -1)
        return res

