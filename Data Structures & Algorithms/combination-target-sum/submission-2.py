class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        def dfs(sum,i):
            if sum==target:
                res.append(curr.copy())
                return 
            
            if sum>target or i>=len(nums):
                return 

            curr.append(nums[i])
            dfs(sum+nums[i],i)

            curr.pop()
            dfs(sum,i+1)

        dfs(0,0)
        return res



      