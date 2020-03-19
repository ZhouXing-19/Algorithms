class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        # dp 的含义：但size 为j时，背包里能否被恰好塞满
        dp = [0] * (m+1)
        #注意初始化：0总是可以被塞满的

        dp[0]=1
        for item in A:
            #注意是倒序遍历
            for j in reversed(range(m+1)):
                #这个判断条件最重要
                if j >= item and dp[j-item]:
                    dp[j] = 1
    ## 对于fixed的一件东西，看当背包容量到多小才不能把它放进去了
    ## max 中的两种情况： dp[j - item] + item -> 放； dp[j - 1] -> 不放
        for maxv in reversed(range(m+1)):

            if dp[maxv]:
                res = maxv
                break
        print(dp)
        return res

m = 10
A = [3,4,8,5]
print(Solution().backPack(m,A))


