class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0]*cols for _ in range(2)]
        for j in range(cols):
            if obstacleGrid[0][j] ==1:
                break
            else:
                dp[0][j] = 1
        for i in range(1,rows):
            for j in range(cols):
                if obstacleGrid[i][j] ==1:
                    dp[i%2][j] = 0
                    continue
                if j == 0:
                    dp[i%2][j] = dp[(i-1)%2][j]
                else:
                    dp[i%2][j] = dp[(i-1)%2][j] + dp[i%2][j-1]
        return dp[(rows-1)%2][j]

