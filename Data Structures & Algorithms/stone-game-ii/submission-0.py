class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        suffix=[0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i]=suffix[i+1]+piles[i]
        dp={}
        def dfs(i,M):
            if i>=n:
                return 0
            if i+2*M>=n:
                return suffix[i]
            if (i,M) in dp:
                return dp[(i,M)]
            score=0
            for X in range(1,2*M+1):
                opps=dfs(i+X,max(M,X))
                myscore=suffix[i]-opps
                score=max(score,myscore)
            dp[(i,M)]=score
            return dp[(i,M)]
        return dfs(0,1)
                