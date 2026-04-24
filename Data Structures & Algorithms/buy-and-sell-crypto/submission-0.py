class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = 0
        max_prices = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[min_prices]:
                prices[min_prices] = prices[i]
            if prices[i] - prices[min_prices] > max_prices:
                max_prices = prices[i] - prices[min_prices] 
        return max_prices



        