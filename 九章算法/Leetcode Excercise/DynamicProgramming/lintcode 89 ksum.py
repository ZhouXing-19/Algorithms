class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    # 在数组A中选择k个数，和为target,求有几种取法
    def kSum(self, A, k, target):
        # write your code here
        if k==0 and target!=0:
            return None
        if k==0 and target==0:
            return 1
        if k>len(A):
            return None
        #dp[i][j][l]: 从前i个数里取j个数使得和为l的"取法" len（A) x k x target
        dp = [[[0]*(target+1) for _ in range(k+1)] for _ in range(len(A)+1)]
        for i in range(len(A)+1):
            dp[i][0][0] = 1
        for i in range(1,len(A)+1):
            for j in range(1,k+1):
                for l in range(target+1):
                    if l>=A[i-1]:
                        # 取第i个数+不取第i个数
                        dp[i][j][l] = dp[i-1][j][l] + dp[i-1][j-1][l-A[i-1]]
                    else:
                        dp[i][j][l] = dp[i-1][j][l]
        return dp[len(A)][k][target]


