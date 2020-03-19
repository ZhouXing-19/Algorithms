class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] == 0:
                    right += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
            else:
                left += 1
                right += 1
        return nums

s = Solution()
nums = [0]
print(s.moveZeroes(nums))