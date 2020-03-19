class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if len(A)==0 or len(V)==0:
            return 0
        size = len(A)
        dp = [0]*(m+1)
        # 注意这里不需要dp[0] = 1,因为这不是判断能不能塞满而是最大值问题
        for i in range(size):
            for j in reversed(range(1,m+1)):
                if j>=A[i]:
                    # 不同的i， 同样的j会重复。比较加入这个i还是另一个i好。
                    dp[j] = max(dp[j],dp[j-A[i]]+V[i])
        return dp[m]