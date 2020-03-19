class Solution:
    def numDistinct(self, s,t):
        #题目： s里有多少子序列 == t
        #dp[i][j]: s[i:]里有多少子序列== t[j:]
        #目标：dp[0][0]
        lenS = len(s)
        lenT = len(t)
        #初始化： 如果i==lenS, dp[i][j] \forall j = 0
        #如果j==lenT, dp[i][j] \forall i = 1
        dp = [[0]*(lenT+1) for _ in range(lenS+1)]
        for j in range(lenT+1):
            dp[lenS][j] = 0
        for i in range(lenS+1):
            dp[i][lenT] = 1

        #If s[i] != t[j], dp[i][j] = dp[i+1][j]
        #If s[i] == t[j], dp[i][j] = dp[i+1][j+1]（不删s[i]) + dp[i+1][j] （删s[i])
        # 注意遍历的顺序： 先i后j
        for i in reversed(range(lenS)):
            for j in range(lenT):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j]+ dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]

    ## 滚动数组优化方案。 考虑到其实i只考虑后一次，其实可以删去这个维度。

    def numDistinct2(self, s, t):
        dp = [0] * (lenT+1)
        dp[lenT] = 1
        for i in reversed(range(lenS)):
            for j in range(lenT):
                if s[i] == t[j]:
                    dp[j] += dp[j+1]
        #dp 的更新只依赖与j这一个维度，因为本质上是s移动指针，向t看齐。
