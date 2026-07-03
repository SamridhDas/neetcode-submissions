class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('infinity')
        l=0
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                res=min(r-l+1,res)
                total-=nums[l]
                l+=1
        if res==float('infinity'):
            return 0
        else:
            return res
    