class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def search(self, i, j, dp, A):
        if i >= j:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        minv = float('inf')
        sumv = sum(A[i:j+1])
        for k in range(i, j):
            minv = min(minv, self.search(i, k, dp, A) + self.search(k + 1, j, dp, A) + sumv)
        dp[i][j] = minv
        return dp[i][j]

    def stoneGame(self, A):
        # write your code here
        size = len(A)
        ## KEY: size+1, not size
        dp = [[0] * (size+1) for _ in range(size+1)]
        for i in range(size):
            dp[i][i] = 0
        res = self.search(0, size - 1, dp, A)
        #print(dp)
        return res

A = [3,4,3]
print(Solution().stoneGame(A))