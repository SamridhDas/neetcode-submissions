class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(start,path):
            if len(path)==len(nums):
                res.append(path[:])
                return 
            for i in range(0,len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(i+1,path)
                    path.pop()
        dfs(0,[])
        return res

       

                


        