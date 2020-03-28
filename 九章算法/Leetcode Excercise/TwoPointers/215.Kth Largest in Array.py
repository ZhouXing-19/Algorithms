import random
#具体解释见手写笔记
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = self.select(nums,0,len(nums)-1,k)
        return res

    def partition(self,nums,left,right,pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        late = left
        for early in range(left,right):
            if nums[early] < pivot:
                nums[early], nums[late] = nums[late],nums[early]
                late += 1
        nums[right],nums[late] = nums[late],nums[right]
        return late

    def select(self,nums,left,right,k):
        if left == right:
            return nums[left]
        size = len(nums)
        pivot_index = random.randint(left, right)
        par_index = self.partition(nums,left,right,pivot_index)
        if par_index == size - k:


            return nums[size-k]
        elif par_index < size - k: #右边数多
            return self.select(nums,par_index+1,right,k)
        else:
            return self.select(nums,left,par_index-1,k)

nums = [3,2,1,5,6,4]
k = 2
res = Solution().findKthLargest(nums,k)