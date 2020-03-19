class Solution:
    def change(self, amount,changes):
        size = len(changes)
        if size==0 or amount<=0:
            return

        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in changes:
            for i in reversed(range(1,amount+1)):
                k = 1
                while i-k*coin>=0:
                    dp[i] += dp[i-k*coin]
                    k += 1
        return dp[-1]
amount = 20
changes = [2,5,10]
Solution().change(amount,changes)





