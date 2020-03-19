class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        # write your code here
        dp = [-1] * max((n + 1),4)
        dp[0] = False
        dp[1] = True
        dp[2] = True
        dp[3] = False
        res = self.search(dp, n)
        print(dp)
        return res

    def search(self, dp, n):

        if dp[n] != -1:
            return dp[n]
        if self.search(dp,n -2) and self.search(dp,n-3) or self.search(dp,n-3) and self.search(dp,n-4):
            dp[n] = True
        else:
            dp[n] = False
        return dp[n]


print(Solution().firstWillWin(1))