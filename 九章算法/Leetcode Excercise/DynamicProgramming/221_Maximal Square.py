class Solution:
    def maximalSquare(self, matrix):
        nrow = len(matrix)
        ncols = len(matrix[0])
        if nrow == 0:
            return 0
        dp = [[0]*ncols]*2
        maxsquare = 0
        #建立 2 x ncols的数组
        for j in range(cols):
            if matrix[0][j] == 1:
                dp[0][j]=1
                maxsquare = 1
        for i in range(1,nrow):
            for j in range(ncols):
                if j == 0:
                    dp[i%2][j] =1
                    maxsquare = max(maxsquare,dp[i%2][j])
                else:
                    if matrix[i][j] == 1:
                        dp[i%2][j] = min(dp[(i-1)%2][j-1],dp[(i-1)%2][j],dp[i%2][j-1])+1
                        maxsquare = max(maxsquare,dp[i%2][j])
                    else:
                        dp[i % 2][j] = 0
        return maxsquare


