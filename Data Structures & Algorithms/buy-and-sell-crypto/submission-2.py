class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        items = prices
        best_result = 0
        lowest_item = items[0]

        for current_item in items:
            if current_item < lowest_item:
                lowest_item = current_item
            potential_result = current_item - lowest_item
            best_result = max(best_result, potential_result)

        return best_result