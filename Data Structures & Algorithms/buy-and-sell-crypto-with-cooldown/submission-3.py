class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold = -float("infinity")
        rest = 0
        sold = 0

        for price in prices:
            prev_hold = hold
            hold = max(hold, rest - price)
            rest = max(rest, sold)
            sold = prev_hold + price
        return max(rest, sold)
        