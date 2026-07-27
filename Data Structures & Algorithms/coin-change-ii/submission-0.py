class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)):
            val=coins[i]
            for v in range(val,amount+1):
                dp[v]=dp[v]+dp[v-val]
        return dp[amount]