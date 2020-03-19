class Solution:
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*(cols+1) for _ in range(2)]
        dp[0][0] = grid[0][0]
        for j in range(1,cols):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1,rows):
            dp[i%2][0] = dp[(i-1)%2][0] + grid[i][0]
            for j in range(1,cols):
                dp[i%2][j] = min(dp[i%2][j-1],dp[(i-1)%2][j])+grid[i][j]

        return dp[(rows-1)%2][cols-1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(Solution().minPathSum(grid))