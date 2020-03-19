
class Solution:
    def QuickSort(self,nums):
        if not nums:
            return None
        return self.helper(nums,0,len(nums)-1)

    def helper(self,nums,start,end):
        if start >= end:
            return
        left, right = start, end
        pivot = nums[int((start + end) / 2)]

        # When comparing left and right, make sure to have <= instead of <
        # We need to avoid left = right = start and end = start +1 situation.
        # Since then the second helper (self.helper(nums,left,end) will be exactly the same as (self.helper(nums,start,end))
        while left<= right:

            while left<=right and nums[left]<pivot:
                left += 1
            while left<=right and nums[right]>pivot:
                right -= 1
            if left<=right:
                nums[left], nums[right] = nums[right],nums[left]
                left += 1
                right -=1
        self.helper(nums,start,right)
        self.helper(nums,left,end)

s = Solution()
nums = [1,2,-3,1,9,0,10]
s.QuickSort(nums)
nums