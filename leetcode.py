# Solutions for Leet Code Problems

# 88 Merge Sorted Array

"""
1. We want to merge two sorted array into a combined sorted array
2. We are tempted to make another array num_temp that stores the sorted elements but this will take more memory
3. A better approach would be to exploit the additional space at the tail end of the array nums1
4. We should thus start by comparing the largest values and storing them at the end of nums1 and making our way to the smaller values

"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Initialize pointer to last (null) element in nums1
        last = m + n - 1

        # Initialize pointer of last real elements in nums1 and 2 that are yet to be compared
        i = m - 1
        j = n - 1

        # while loop
        while m > 0 and n > 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                m -= 1
            else:
                nums1[last] = nums2[j] 
                n -= 1
            last -= 1

        # Fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[j]
            n, last = n - 1, last - 1


# 27 Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i