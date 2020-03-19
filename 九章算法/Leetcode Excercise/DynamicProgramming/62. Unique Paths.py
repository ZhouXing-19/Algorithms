class Solution:
    def uniquePaths(self, m, n):
        if m==0 or n==0:
            return 1
        dp = [[0]*(n+1) for _ in range(2)]
        dp[0][0] = 1
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]
        for i in range(1,m):
            for j in range(n):
                if j ==0:
                    dp[i%2][j] = dp[(i-1)%2][j]
                else:
                    dp[i%2][j] = dp[(i-1)%2][j]+dp[i%2][j-1]
        return dp[(m-1)%2][n-1]

m = 7
n = 3
print(Solution().uniquePaths(m,n))