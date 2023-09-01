# 122 Best Time to Buy and Sell Stock II

"""
Solution 1 

Time Complexity: O(n)
Space Complexity: O(1)

Intuition and Approach
- Realize we only need to concern ourself with prices increase. Max profit is earned when EVERY rises in prices is captured and EVERY lose is ignored
- Set a variable max_profit designed to keep track of profit earned thus far.
- Iterate over prices and update max_profit if price goes up (i.e the current price > previous price) 
- Return max_profit

Special Notes: 
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit
