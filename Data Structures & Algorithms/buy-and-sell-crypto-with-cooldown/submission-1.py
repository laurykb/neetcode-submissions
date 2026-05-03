class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -float("infinity")
        rest = 0
        sold = 0

        for price in prices:

            prev_hold = hold
            hold = max(prev_hold, rest - price)
            rest = max(rest, sold)
            sold = prev_hold + price
        
        return max(sold, rest)
