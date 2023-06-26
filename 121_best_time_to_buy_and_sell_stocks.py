# 121 Best Time to Buy and Sell Stocks
"""
Solution 1 
Runtime: 807 ms (beats 98.61%)
Memory: 22.5 MB (beats 87.47%)

Time Complextiy: O(n)
Space Complexity: O(1)

Intuition and Approach
- Initialize two counters lowest_price and max_profit. 
- Iterate over the prices array
- If the current price is less than or equal to the lowest price, set lowest_price = current_price
- If (current_price - lowest_price) > max_profit, update max_profit. 
- Finally, return max_profit
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        lowest_price, max_profit = prices[0], 0
        
        for current_price in prices:
            if current_price < lowest_price:
                lowest_price = current_price
            elif (current_price - lowest_price) > max_profit:
                max_profit = current_price - lowest_price
        
        return max_profit
