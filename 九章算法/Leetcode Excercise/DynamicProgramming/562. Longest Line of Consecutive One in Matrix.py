class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if len(M) == 0:
            return 0
        if len(M[0]) == 0:
            return 0
        rows = len(M)
        cols = len(M[0])
        maxlength = 0
        dp  = [[0]*4 for _ in range(cols+1)]
        #这里只用2维dp的原因是，for循环已经是从上到下的顺序了。在计算一个点horizontal line，我们只向左看。计算 vertical line，只向上看。
        #计算 对角线，只向左上角看。 计算反对角线，只看右上角。在上下方向，我们已经确定了，所以可以删除行的维度。 （i)
        for i in range(rows):
            old = 0
            for j in range(cols):
                if M[i][j] == 1:
                    #如果这个点是1（其余方向都是0），其位置满足边界条件，则可视为各个方向的起点，所以各个方向都是1。
                    dp[j][0] = dp[j-1][0]+1 if j>0 else 1
                    dp[j][1] = dp[j][1]+1 if i>0 else 1

                    # 这里正对角线的原因是，当i不变，j从左到右时，j+1的左对角线会依赖j在更新前（i-1）状态的对角线。
                    # 但如果这个点是0，这一行在i行的对角线就是0。所以要用一个old保存i-1行的对角线状态。

                    temp = dp[j][2]
                    dp[j][2] = old+1 if i>0 and j>0 else 1
                    old = temp
                    dp[j][3] = dp[j+1][3]+1 if i>0 and j<cols-1
                    maxlength = max(maxlength,dp[j][0],dp[j][1],dp[j][2],dp[j][3])
                else:

                    old = dp[j][2]
                    for k in range(3):
                        dp[j][k]=0
        return maxlength