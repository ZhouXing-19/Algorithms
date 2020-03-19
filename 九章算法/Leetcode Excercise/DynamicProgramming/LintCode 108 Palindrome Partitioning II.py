class Solution:
    def isPalindrome(self,s):
        # table: table[i][j]: tell if s[i:j] is palindrome
        size = len(s)
        table = [[False]*size for _ in range(size)]
        for i in range(size):
            table[i][i] = True
            if i<size-1 and s[i]==s[i+1]:
                table[i][i+1] = True
        # 先fix长度
        # 再fix start的终点，保证start + length < size
        for length in range(2,size):
            for start in range(size-length):
                end = start + length
                table[start][end] = table[start+1][end-1] and (s[start] == s[end])
        return table

    def minicut(self,s):
        #dp[i]: 前i个字符串得到分割片段均为回文的最小cut count
        table = self.isPalindrome(s)
        dp = [0]*(len(s)+1)
        # 先预设所有的前i个字符串都没有任何回文substring
        # 注意端点：如果只有1个字符串，不需要分割。所以dp[1] = 0
        # 需要从0开始： 因为在31行有一个+1。 要考虑s = "aaaa" 的情况，这时候输出应该是0。
        for i in range(0,len(s)+1):
            dp[i] = i-1

        for end in range(1,len(s)+1):
            for start in range(0,end):
                if table[start][end-1]:
                    dp[end] = min(dp[end],dp[start]+1)
        return dp[len(s)]

