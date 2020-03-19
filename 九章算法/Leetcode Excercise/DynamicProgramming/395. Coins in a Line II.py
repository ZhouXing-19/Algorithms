class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        size = len(values)
        dp = [0] * (size + 1)
        # dp[i]: the max achievable value from i to the end of line
        if size < 3:
            return True
        dp[size] = 0
        dp[size - 1] = values[size - 1]
        dp[size - 2] = values[size - 1] + values[size - 2]
        dp[size - 3] = values[size - 2] + values[size - 3]

        for i in reversed(range(size - 3)):
            #我取一个，对方取一个或者两个 -> i+2 或 i+3 ； 我取两个，对方取两个或3个 -> i+3 或 i+4
            dp[i] = max(min(dp[i + 2], dp[i + 3]) + values[i], min(dp[i + 3], dp[i + 4]) + values[i] + values[i + 1])

        return dp[0] > sum(values) - dp[0]

