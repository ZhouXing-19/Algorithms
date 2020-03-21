class Solution:
    def longestCommonSubsequence(self, text1,text2):
        # dp[i][j]: LCS for first i chars in text1 and first j chars in text2
        size1 = len(text1)
        size2 = len(text2)
        dp = [[0]*(size2+1) for _ in range(size1+1)]

        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[size1][size2]


text1 ="oxcpqrsvwf"
text2 = "shmtulqrypy"
print(Solution().longestCommonSubsequence(text1,text2))
#
# size1 = 5
# size2 = 3
# i = 3
# j = 3