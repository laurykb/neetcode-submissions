class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # on va de 0 --- > amount et tous les élements sont de amount + 1
        dp[0] = 0 # si on veut obtenir 0 ça prend 0 coins
# for every amoutn a
        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
        