class Status:
    def __init__(self,v,f):
        self.value = v
        self.flag = f

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def memorySearch(self,i,j,dp,n):
        if i>j:
            return 0
        if dp[(i,j)].flag:
            return dp[(i,j)].value
        else:
            dp[(i,j)] = Status(max(min(self.memorySearch(i+2,j,dp,n),self.memorySearch(i+1,j-1,dp,n))+n[i],
                        min(self.memorySearch(i+1,j-1,dp,n),self.memorySearch(i,j-2,dp,n))+n[j]),True)
            return dp[(i,j)].value

    def firstWillWin(self, n):
        size = len(n)
        dp = {}
        for i in range(size):
            for j in range(i,size):
                if i==j:
                    dp[(i,j)] = Status(n[i],True)
                elif j==i+1:
                    dp[(i,j)] = Status(max(n[i],n[j]),True)
                else:
                    dp[(i,j)] = Status(0,False)
        res = self.memorySearch(0,size-1,dp,n)
        return sum(n)<2*res
n = [1,4,9,0]
print(Solution().firstWillWin(n))