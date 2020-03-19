class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]

        dp = [[0]*n for _ in range(2)]
        for i in range(n):
            dp[(n-1)%2][i] = triangle[n-1][i]

        for i in reversed(range(n-1)):
            print(dp)
            # 注意是i+1
            for j in range(i+1):
                dp[i%2][j] = min(dp[(i+1)%2][j],dp[(i+1)%2][j+1]) + triangle[i][j]

        return dp[0][0]

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(Solution().minimumTotal(triangle))