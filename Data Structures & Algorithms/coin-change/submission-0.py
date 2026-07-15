class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('infinity')]*(amount+1)
        dp[0]=0
        for i in range(len(coins)):
            value=coins[i]
            for v in range(value,amount+1):
                dp[v]=min(dp[v],dp[v-value]+1)
        if dp[amount]==float('infinity'):
            return -1
        else:
            return dp[amount]