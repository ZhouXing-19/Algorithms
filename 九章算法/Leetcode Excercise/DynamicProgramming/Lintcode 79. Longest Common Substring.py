class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """

    def longestCommonSubstring(self, A, B):
        # write your code here
        size1 = len(A)
        size2 = len(B)
        #dp[i][j]: LCS for substrings **end with A[i]** and **ended with B[j]**
        maxLCS = 0

        dp = [[0]*(size2+1) for _ in range(size1+1)]
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if A[i-1] != B[j-1]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j-1]+1
                    maxLCS = max(maxLCS,dp[i][j])
        return maxLCS

A = "ABCS"
B = "CSE"
print(Solution().longestCommonSubstring(A,B))