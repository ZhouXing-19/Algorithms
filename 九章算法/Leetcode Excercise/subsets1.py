class Solution:
    def Subset(self,A,results,subset,i):
        size = len(A)
        if len(subset)>0:
            results.append(subset[:])
        #print("subset:", subset)


        for j in range(i,size):
            subset.append(A[j])
            self.Subset(A,results,subset,j+1)
            subset.pop()

    def main(self,A):
        sorted_A = sorted(A)
        init_set = []
        #global results
        results = []
        self.Subset(sorted_A,results,init_set,0)
        return results


s = Solution()
results = s.main([1,2,3])
print(results)

#
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first=0, curr=[]):
#             # if the combination is done
#             if len(curr) == k:
#                 output.append(curr[:])
#             for i in range(first, n):
#                 # add nums[i] into the current combination
#                 curr.append(nums[i])
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
#
#         output = []
#         n = len(nums)
#         for k in range(n + 1):
#             backtrack()
#         return output

