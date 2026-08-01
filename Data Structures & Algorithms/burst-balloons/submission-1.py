class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a=[1]+nums+[1]
        n=len(a)
        dp=[[0]*n for i in range(n)]
        for x in range(2,n):
            for i in range(n-x):
                j=i+x
                for k in range(i+1,j):
                    dp[i][j]=max(dp[i][j],a[k]*a[i]*a[j]+dp[i][k]+dp[k][j])
        return dp[0][n-1]