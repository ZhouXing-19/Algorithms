class Solution:
    def search(self, coins, amount, dp):

        if dp[amount] != -1:
            return dp[amount]
        min_times = float('inf')
        for coin in coins:
            if amount - coin >= min(coins):
                min_times = min(min_times, self.search(coins,amount-coin,dp) + 1)
        dp[amount] = min_times
        return dp[amount]

    def coinChange(self, coins, amount):
        if len(coins) < 1:
            return -1
        min_coin = min(coins)
        if amount < min_coin:
            return -1
        dp = [-1] * (amount+1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        res = self.search(coins, amount, dp)
        return res

coins = [1, 2, 5]
amount = 13
print(Solution().coinChange(coins,amount))