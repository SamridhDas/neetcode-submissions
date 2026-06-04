class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def can(largest):
            s=1
            curr=0
            for num in nums:
                curr+=num
                if curr>largest:
                    s+=1
                    if s>k:
                        return False
                    curr=num
            return True 
           
                
        


        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            m=(l+r)//2
            if can(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res

