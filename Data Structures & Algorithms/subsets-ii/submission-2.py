class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(start,path):
            nums.sort()
            res.append(path[:])

            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        dfs(0,[])
        return res
