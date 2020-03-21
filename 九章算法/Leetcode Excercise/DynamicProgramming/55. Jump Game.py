# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
class Solution:
    def canJump1(self, nums):
        # dp[i]: boolean: if the ith position is accessible
        n = len(nums)
        dp = [False] * (n)
        dp[0] = True
        for i in range(1,n):
            for j in range(i):
                if dp[j] and j+nums[j] >= i:
                    dp[i] = True
                    break
        #print(dp)
        return dp[n-1]

        def canJump(self, nums: List[int]) -> bool:
            if len(nums) < 0 or not nums:
                return False

            farthest = nums[0]
            for i in range(len(nums)):
                if i <= farthest and nums[i] + i >= farthest:
                    farthest = nums[i] + i
            return farthest >= len(nums) - 1


# This should work but it exceeds time limit!!


nums = [3,2,1,0,4]
print(Solution().canJump(nums))