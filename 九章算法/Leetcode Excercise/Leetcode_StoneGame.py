class Status:
    def __init__(self, v, f):
        self.value = v
        self.flag = f


class Solution:
    def search(self, piles, i, j, dp):
        if i > j:
            return 0
        if dp[i][j].flag:
            return dp[i][j].value
        dp[i][j] = Status(max(min(self.search(piles, i + 2, j, dp), self.search(piles, i + 1, j - 1, dp)) + piles[i],
                              min(self.search(piles, i + 1, j - 1, dp), self.search(piles, i, j - 2, dp)) + piles[j]),
                          True)
        return dp[i][j].value

    def stoneGame(self, piles):
        size = len(piles)
        dp = [[0] * (size + 1) for _ in range(size + 1)]
        for i in range(size):
            for j in range(i, size):
                if i == j:
                    dp[i][j] = Status(piles[i], True)
                elif i == j - 1:
                    dp[i][j] = Status(max(piles[i], piles[j]), True)
                else:
                    dp[i][j] = Status(0, False)
        res = self.search(piles, 0, size - 1, dp)
        return sum(piles) < res * 2


piles = [5,3,4,5]
print(Solution().stoneGame(piles))