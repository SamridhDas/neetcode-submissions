class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[None]*n
        maxp=nums[0]
        minp=nums[0]
        res=nums[0]
        
        for i in range(1,n):
            if nums[i]<0:
                maxp,minp=minp,maxp
            maxp=max(nums[i],maxp*nums[i])
            minp=min(nums[i],minp*nums[i])
            res=max(maxp,res)
        return res