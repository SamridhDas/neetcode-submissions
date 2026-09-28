class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for v in range(target+1):
            for num in nums:
                if num<=v:
                    dp[v]=dp[v]+dp[v-num]
        return dp[target]
