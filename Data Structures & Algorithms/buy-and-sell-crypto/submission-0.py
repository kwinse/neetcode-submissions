class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            potential = prices[i] - lowest
            profit = max(profit, potential)

        return profit