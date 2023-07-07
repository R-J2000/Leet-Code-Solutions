# 274 H-Index

"""
Solution 1 (Bad Time Complexity)

Time Complexity: O(n^2)
Space Complexity: O(1)

Intuition and Approach
- Set the h-index to the total number of citations. We will try for the max possible h-index val and decrement iteratively until we get to 0. In which case return 0.
- Iterate over the citations. If a particular citation is above the current h-index, update counter.
- After iteration, check if counter >= h-index. If yes, this means at least h papers have been cited h times.
- If not, decrement h-index and try for a smaller h-index value

"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        h_index = len(citations)

        while h_index != 0:
            counter = 0
            for i in citations:
                if i >= h_index:
                    counter += 1
                
            if counter >= h_index:
                return h_index
            else:
                h_index -= 1
        
        return 0

"""
Solution 2 (Sorting)

Time Complexity: O(nlog(n))
Space Complexity: O(1)

Intuition and Approach
- Sort citations
- Compare citations to its index. If index >= citations return index (h papers that have each been cited at least h times.)
- Otherwise, return len(citations). A scenario where citations are always greater than the index. He the h-index will be bound not by the number of citations, but by the number of papers


"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse = True)

        ind = 0
        for ind, citation in enumerate(citations):
            if ind >= citation:
                return ind
        return len(citations)
