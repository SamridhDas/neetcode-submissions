class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        p=target+total
        if p%2:
            return 0
        if abs(target)>total:
            return 0
        dp=[0]*(p//2+1)
        dp[0]=1
        for val in nums:
            for v in range(p//2,val-1,-1):
                dp[v]=dp[v]+dp[v-val]
        return dp[p//2]
        