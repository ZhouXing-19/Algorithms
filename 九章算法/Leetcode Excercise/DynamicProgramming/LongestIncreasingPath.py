class Solution:
    def longestIncreasingPath(self, matrix):
        res = 1
        nrow = len(matrix)
        ncol = len(matrix[0])
        dp = [[0] * ncol for _ in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                res = max(res, self.search(matrix, i, j, dp))
        print(dp)
        return res

    def search(self, matrix, i, j, dp):
        print("i: ",i ,"j: ",j ,dp)
        if dp[i][j] != 0:
            return dp[i][j]

        nrow = len(matrix)
        ncol = len(matrix[0])
        maxlen = 1

        shifts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta_x, delta_y in shifts:
            x = i + delta_x
            y = j + delta_y
            if x >= 0 and x < nrow and y >= 0 and y < ncol and matrix[i + delta_x][j + delta_y] < matrix[i][j]:
                maxlen = max(maxlen, self.search(matrix, x, y, dp) + 1)

        dp[i][j] = maxlen
        return dp[i][j]

nums = [[1,2,3],
        [8,9,4],
        [7,6,5]]
Solution().longestIncreasingPath(nums)

