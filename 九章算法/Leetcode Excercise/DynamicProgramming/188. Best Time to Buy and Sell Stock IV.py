#Design an algorithm to find the maximum profit. You may complete at most k transactions.
class Solution:
    def maxProfit(self, k, prices):
        size = len(prices)
        if size<2:
            return 0
        if k>=size/2:
            #回到可以交易无限次的情况
            ans = 0
            for i in range(1,size):
                gain  = prices[i]-prices[i-1]
                if gain>0:
                    ans += gain
            return ans

        #mustsell[i][j] : 在第i天必须要卖且从0-i天最多交易j次的最大利润
        #globalbest[i][j]: 在第i天不一定要卖，且从0-i天最多交易j次的最大利润
        #状态转移： mustsell[i][j] = max(mustsell[i-1][j] + gain , globalbest[i-1][j-1]+gain)
        #globalbest[i][j] = mustsell[i][j] + globalbest[i-1][j]
        mustsell = [0] * (k+1)
        globalbest = [0] * (k+1)

        for i in range(1,size):
            gain = prices[i] - prices[i-1]
            #注意这里的倒序
            for j in reversed(range(1,k+1)):
                mustsell[j] = max(mustsell[j],globalbest[j-1])+gain
                globalbest[j] = max(mustsell[j],globalbest[j])
        return globalbest[k]


