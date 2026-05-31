class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]

        def dfs(i,sum):
            if sum==target:
                res.append(curr.copy())
                return 
            
            if i>=len(nums) or sum>target:
                return 
            curr.append(nums[i])
            dfs(i,sum+nums[i])

            curr.pop()
            dfs(i+1,sum)
        dfs(0,0)
        return res