class Solution:
    def climbStairs(self, n: int) -> int:
        dp={0:1,1:1}
        def solve(x):
            if x in dp:
                return dp[x]
            dp[x]=solve(x-1)+solve(x-2)
            return dp[x]
        solve(n)
        return dp[n]