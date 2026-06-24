class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        nums.sort(reverse=True)
        target=sum(nums)//k
        used=[False]*len(nums)

        def dfs(start,k,sub):
            if k==0:
                return True
            if sub==target:
                return dfs(0,k-1,0)
            for i in range(start,len(nums)):
                if used[i] or sub+nums[i]>target:
                    continue
                used[i]=True
                if dfs(i+1,k,sub+nums[i]):
                    return True
                used[i]=False
            return False
        return dfs(0,k,0)
            