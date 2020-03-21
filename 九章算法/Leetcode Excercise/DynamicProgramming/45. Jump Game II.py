class Solution:
    def jump(self, nums):
        size = len(nums)
        if size == 0:
            return 1
        # dp[i]: the minimum step to the ith position
        dp = [float('inf')]*size
        dp[0] = 0
        for i in range(1,size):
            for j in range(i):
                if dp[j]!= float('inf') and j+nums[j]>=i:
                    dp[i] = min(dp[i],dp[j]+1)
        if dp[size-1] == float('inf'):
            return None
        return dp[size-1]

nums = [2,3,1,1,4]
print(Solution().jump(nums))
