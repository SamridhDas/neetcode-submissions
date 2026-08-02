class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s=sum(stones)
        dp=[False]*(s//2+1)
        dp[0]=True
        for stone in stones:
            for x in range(s//2,stone-1,-1):
                dp[x]=dp[x] or dp[x-stone]
        for i in range(s//2,-1,-1):
            if dp[i]:
                return s-2*i