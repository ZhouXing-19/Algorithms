class Solution:
    def lengthOfLIS(self, nums):
        # Solve it by binary search
        # minLast[index]: the minimum ending of lis with length == index
        # claim: minLast is monotonly increasing. You can prove it by contradiction
        if len(nums) == 0:
            return 0

        minLast = [float('inf')] * (len(nums) + 1)
        # Attention Here, the initialization should consider the case that thu number of nums can be negative.
        minLast[0] = -float('inf')
        for i in range(len(nums)):
            index = self.BinarySearch(minLast, nums[i])
            minLast[index] = nums[i]
        print(minLast)

        # Attention here too: len(nums+1)
        for j in reversed(range(len(nums)+1)):
            if minLast[j] != float('inf'):
                return j

    def BinarySearch(self, lst, num):
        # 找最近的大于（而不是大于等于）num的数
        l, r = 0, len(lst) - 1
        while l!=r:
            # 注意，每次mid在while里面更新！！！
            mid = (l+r)//2
            # 如果是找最近的大于等于的数，把下面的<= 改成 <
            if lst[mid] < num:
                l = mid+1
            else:
                r = mid

        return l







nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))


