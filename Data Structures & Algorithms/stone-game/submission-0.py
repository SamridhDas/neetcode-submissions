class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=[[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=piles[i]
        for x in range(2,n+1):
            for i in range(n-x+1):
                j=i+x-1
                dp[i][j]=max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
        return dp[0][n-1]>0
