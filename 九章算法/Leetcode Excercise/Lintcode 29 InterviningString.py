class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        # dp[i][j]: s1 的前i个字符和 s2的前j个字符能不能组成s3的前 i+k个字符
        if len3 != len1+len2:
            return False
        if len1 == 0:
            if s2 != s3:
                return False
            return True

        if len2 == 0:
            if s1 != s3:
                return False
            return True

        # 注意初始化的维度顺序
        dp = [[False]*(len2+1) for _ in range(len1+1)]

        dp[0][0] = True

        #边界初始化
        for i1 in range(1, len1+1):
            if dp[i1-1][0] and s1[i1-1] == s3[i1-1]:
                dp[i1][0] = True
            else:
                break

        for i2 in range(1, len2+1):
            if dp[0][i2-1] and s2[i2-1] == s3[i2-1]:
                dp[0][i2] = True
            else:
                break

        for i1 in range(1,len1+1):
            for i2 in range(1,len2+1):
                #转移条件
                if s1[i1-1] == s3[i1+i2-1] and dp[i1-1][i2] or \
                    s2[i2-1] == s3[i1+i2-1] and dp[i1][i2-1]:
                    dp[i1][i2] = True
        return dp[len1][len2]

s1  = "aab"
s2  = "a"
s3  = "aaab"
print(Solution().isInterleave(s1,s2,s3))