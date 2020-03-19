class Solution:
    def canPartition(self, nums):
        if len(nums)==0:
            return True
        amount = sum(nums)/2
        if amount != int(amount):
            return False
        amount = int(amount)
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in nums:
            for i in reversed(range(1,amount+1)):
                if i>=coin and dp[i-coin]:
                    dp[i] = 1
        #print(dp)
        return dp[-1]>0

nums = [1,5,5,11]
Solution().canPartition(nums)