class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_result = 0
        lowest_price = prices[0]

        for current_price in prices:
            if current_price < lowest_price:
                lowest_price = current_price
            potential_result = current_price - lowest_price
            best_result = max(best_result, potential_result)

        return best_result