class Solution:
    def BinarySearch(self, lst, num):
        # 找最近的大于（而不是大于等于）num的数
        l, r = 0, len(lst) - 1
        while l!=r:
            # 注意，每次mid在while里面更新！！！
            mid = (l+r)//2
            # 如果是找最近的大于等于的数，把下面的<= 改成 <
            if lst[mid] <= num:
                l = mid+1
            else:
                r = mid

        return l
lst = [1,2,3,4,5,7,8]
num = 7
print(Solution().BinarySearch(lst,num))