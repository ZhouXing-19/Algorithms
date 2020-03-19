class Solution:

    def findKsmallest(self,nums,k):
        if not nums:
            return -1
        return self.helper(nums,0,len(nums)-1,k)
    def helper(self,nums,start,end,k):
        if start>=end:
            return
        l = start
        r = end
        m = int((l+r)/2)
        pivot = nums[m]
        while l<=r:
            while l<=r and nums[l]>pivot:
                l+=1
            while l<=r and nums[r]<pivot:
                r-=1
            if l<=r:
                nums[l], nums[r] = nums[r],nums[l]
                l+=1
                r-=1

        if k>r+1 and k<=l+1:
            return nums[k-1]
        elif k<=r+1:
            self.helper(nums,start,r,k)
        else:
            self.helper(nums,k-l+1,end,k)

        self.helper(nums,start,r,k)
        self.helper(nums,l,end,k)


s = Solution()
nums = [23,4,5,2,4,54]
print(s.findKthLargest(nums,2))